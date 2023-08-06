"""
```py
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sql_fixture import fixture

BaseModel = declarative_base()

class User(BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(150), nullable=False, unique=True)
    email = Column(String(254), unique=True)


def main():
    engine = create_engine('sqlite://')
    BaseModel.metadata.create_all(engine)
    connection = engine.connect()
    session = Session(bind=connection)

    fixture = '''
    - User:
      - username: xyz
        email: xyz@example.com
      - username: abc
        email: abv@example.com
    '''
    fixture.load(BaseModel, session, fixture)

    print('\n'.join(u.username for u in session.query(User).all()))

if __name__ == '__main__':
    main()
```
"""

import logging
import sys
from functools import lru_cache

import sqlalchemy
import yaml
from sqlalchemy.orm.relationships import RelationshipProperty

from sql_fixture.logger import Colors, Formatter

# LOGGING CONFIGURATION
log = logging.getLogger()
log_format = (
    f"{Colors.Fore.GREEN}%(asctime)-s "
    f"{Colors.LEVEL_COLOR}%(levelname).1s "
    f"{Colors.Fore.MAGENTA}%(filename)-s:%(lineno)03d "
    f"{Colors.LEVEL_COLOR}- %(message)s"
)
formatter = Formatter(
    fmt=log_format, arg_start_color=Colors.Fore.WHITE, arg_end_color=Colors.LEVEL_COLOR
)
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
log.addHandler(handler)


def from_registry(Base, model_name):
    """Compatibility for SQLAlchemy

    https://github.com/sqlalchemy/sqlalchemy/commit/450f5c0d6519a439f4025c3892fe4cf3ee2d892c

    :param Base: Base class
    :param model_name: name of model
    """
    if hasattr(Base, "_decl_class_registry"):  # SQLAlchemy < 1.4
        return Base._decl_class_registry[model_name]  # pragma: no cover
    else:
        return Base.registry._class_registry[model_name]


class Store:
    """Simple key-value store

    Key might be a dot-separated where each name after a dot
    represents and attribute of the value-object.

    Example:
        store.put("foo", Foo())
        store.put("foo.bar", Bar())
        store.get("foo.bar")  # returns Bar()
    """

    def __init__(self):
        self._store = {}

    def get(self, key):
        parts = key.split(".")
        ref_obj = self._store[parts.pop(0)]
        while parts:
            ref_obj = getattr(ref_obj, parts.pop(0))
        return ref_obj

    def put(self, key, value):
        assert key not in self._store, f"Duplicate key:{key}"
        self._store[key] = value


@lru_cache()
def _get_rel_col_for(src_model, target_model_name):
    """find the column in src_model that is a relationship to target_model `@return` column name

    :param src_model: SqlAlchemy Mapper
    :param target_model_name: name of target model

    :return: column name

    :raises ValueError: if no relationship is found
    """
    # TODO deal with self-referential m2m
    for name, col in src_model._sa_class_manager.items():
        try:
            target = col.property.mapper.class_
            log.info(f"target: {target}")
        except AttributeError:
            continue
        if target.__name__ == target_model_name:
            return name
    msg = "Mapper `{}` has no field with relationship to type `{}`"
    raise ValueError(msg.format(src_model.__name__, target_model_name))


def _create_obj(ModelBase, session, store, model_name, creator, key, values):
    """create obj from values

    :var store (Store):
    :var model_name (str): name of Model/Mapper
    :var creator (str): classmethod name used to create obj, Takes 2 parameters (session, values)
    :var key (str): key for obj in Store
    :var values (dict): column:value

    :return: created object

    :raises ValueError: if error occurs
    """
    # get reference to SqlAlchemy Mapper
    model = from_registry(ModelBase, model_name)

    # scalars will be passed to mapper __init__
    scalars = {}

    # Nested data will be created after container object,
    # container object reference is found by back_populates
    # each element is a tuple (model-name, field_name, value)
    nested = []

    # references "2many" that are in a list
    many = []  # each element is 2-tuple (field_name, [values])

    for name, value in values.items():
        try:
            try:
                column = getattr(model, name).property
            except AttributeError:
                # __init__ param that is not a column
                log.debug(f"skipping {name}")
                scalars[name] = (
                    store.get(value["ref"]) if isinstance(value, dict) else value
                )
                continue

            # simple value assignemnt
            if not isinstance(column, RelationshipProperty):
                scalars[name] = value
                continue

            # relationship
            rel_name = column.mapper.class_.__name__
            if isinstance(value, dict):
                # If column includes a back_populates, we assume
                # the constructor of the nested object takes a reference
                # to its parent.
                if column.back_populates:
                    nested.append([rel_name, column.back_populates, value])
                # If there is no back_populates create the nested object
                # first
                else:
                    scalars[name] = _create_obj(
                        ModelBase, session, store, rel_name, None, None, value
                    )

            elif isinstance(value, str):
                scalars[name] = store.get(value)

            elif isinstance(value, list):
                if not value:
                    continue  # empty list
                # if list element are string they are references
                if isinstance(value[0], str):
                    secondary = getattr(column, "secondary", None)
                    if secondary is None:
                        # assume association object and find other reference
                        tgt_model_name = store.get(value[0]).__class__.__name__
                        rel_model = from_registry(ModelBase, rel_name)
                        col_name = _get_rel_col_for(rel_model, tgt_model_name)
                        refs = [rel_model(**{col_name: store.get(v)}) for v in value]
                    else:
                        refs = [store.get(v) for v in value]
                    many.append((name, refs))

                elif column.back_populates:
                    nested.extend(
                        [rel_name, column.back_populates, v] for v in value
                    )  # pragma: no cover
                else:
                    scalars[name] = [
                        _create_obj(ModelBase, session, store, rel_name, None, None, v)
                        for v in value
                    ]

            else:
                scalars[name] = value

        except Exception as orig_exp:
            raise ValueError(
                f"Error processing {model_name}.{name}={value}\n{str(orig_exp)}"
            ) from orig_exp

    if creator is None:
        creator = "from_fixture" if hasattr(model, "from_fixture") else None

    if creator is None:
        obj = model(**scalars)
    else:
        obj = getattr(model, creator)(session, scalars)

    # add a nested objects with reference to parent
    for rel_name, back_populates, value in nested:
        value[back_populates] = obj
        _create_obj(ModelBase, session, store, rel_name, None, None, value)

    # save obj in store
    if key:
        store.put(key, obj)

    # 2many references
    for field_name, value_list in many:
        setattr(obj, field_name, value_list)

    return obj


def load(ModelBase, session, fixture_text, loader=None):
    """Load fixture data into database

    :param ModelBase: SqlAlchemy declarative base
    :param session: SqlAlchemy session
    :param fixture_text: YAML fixture text
    :param loader: YAML loader

    :return: None
    """
    # make sure backref attributes are created
    sqlalchemy.orm.configure_mappers()

    # Data should be sequence of entry per mapper name
    # to enforce that FKs (__key__ entries) are defined first
    if loader is None:
        loader = yaml.FullLoader
        log.info("Using yaml.FullLoader")
    data = yaml.load(fixture_text, Loader=loader)
    if not isinstance(data, list):
        raise ValueError("Top level YAML should be sequence (list).")

    store = Store()
    for model_entry in data:
        if len(model_entry) != 1:
            log.info(model_entry)
            msg = "Sequence item must contain only one mapper," " found: {}."
            raise ValueError(msg.format(", ".join(model_entry.keys())))

        model_name, instances = model_entry.popitem()
        # model_name can be a simple model name or <Name>:<creator>
        if ":" in model_name:
            model_name, creator = model_name.split(":")
        else:
            creator = None

        if instances is None:
            # Ignore empty entry
            continue
        if not isinstance(instances, list):
            msg = "Mapper `{}` should have a list of instances."
            raise ValueError(msg.format(model_name))
        for fields in instances:
            key = fields.pop("__key__", None)
            obj = _create_obj(
                ModelBase, session, store, model_name, creator, key, fields
            )
            session.add(obj)
    session.commit()
    return store

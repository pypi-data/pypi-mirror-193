import pytest
from sqlalchemy import Column, ForeignKey, Integer, String, Table, create_engine
from sqlalchemy.orm import Session, backref, declarative_base, relationship

BaseModel = declarative_base()

user_friends = Table(
    "user_friends",
    BaseModel.metadata,
    Column(
        "user_id",
        Integer,
        ForeignKey("user.id"),
        nullable=False,
        primary_key=True,
    ),
    Column(
        "friend_id",
        Integer,
        ForeignKey("user.id"),
        nullable=False,
        primary_key=True,
    ),
)

user_instruments = Table(
    "user_instruments",
    BaseModel.metadata,
    Column(
        "user_id",
        Integer,
        ForeignKey("user.id"),
        nullable=False,
        primary_key=True,
    ),
    Column(
        "instrument_id",
        Integer,
        ForeignKey("instrument.id"),
        nullable=False,
        primary_key=True,
    ),
)


class Instrument(BaseModel):
    __tablename__ = "instrument"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True)


class User(BaseModel):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(150), nullable=False, unique=True)
    email = Column(String(254), unique=True)
    roles = relationship("Role")
    friends = relationship(
        "User",
        secondary=user_friends,
        primaryjoin=id == user_friends.c.user_id,
        secondaryjoin=id == user_friends.c.friend_id,
        order_by="User.username",
    )
    instruments = relationship(
        "Instrument",
        secondary=user_instruments,
        order_by="Instrument.name",
    )


class Role(BaseModel):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    user_id = Column(ForeignKey("user.id"), nullable=False)
    user = relationship("User")


class Profile(BaseModel):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    user_id = Column(
        ForeignKey("user.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        unique=True,
    )
    user = relationship(
        "User",
        uselist=False,
        backref=backref("profile", uselist=False, cascade="all, delete-orphan"),
    )

    def __init__(self, nickname=None, the_user=None, **kwargs):
        if nickname is not None and "name" not in kwargs:
            self.name = nickname
        if the_user is not None:
            self.user = the_user
        super().__init__(**kwargs)


class Profile2(BaseModel):
    __tablename__ = "profile2"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    user_id = Column(
        ForeignKey("user.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        unique=True,
    )
    user = relationship(
        "User",
        uselist=False,
        backref=backref("profile2", uselist=False, cascade="all, delete-orphan"),
    )

    def __init__(self, user=None, **kwargs):
        assert user is not None
        self.user = user
        super().__init__(**kwargs)


class Profile3(BaseModel):
    __tablename__ = "profile3"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    user_id = Column(
        ForeignKey("user.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        unique=True,
    )
    # Note relationship has no back_ref
    user = relationship("User", uselist=False)

    def __init__(self, user=None, **kwargs):
        assert user is not None
        self.user = user
        super().__init__(**kwargs)


class Group(BaseModel):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)


class GroupMember(BaseModel):
    __tablename__ = "group_member"
    id = Column(Integer, primary_key=True)
    group_id = Column(
        ForeignKey("group.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    profile_id = Column(
        ForeignKey("profile.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    group = relationship(
        "Group",
        backref=backref("members", cascade="all, delete-orphan"),
    )
    profile = relationship(
        "Profile",
        backref=backref("groups", lazy="dynamic"),
    )


class Genre(BaseModel):
    __tablename__ = "genre"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    group_id = Column(
        ForeignKey("group.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    group = relationship(
        "Group",
        backref=backref("genres", cascade="all, delete-orphan"),
    )


# Custom Table
class Person(BaseModel):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    username = Column(String(150), nullable=False, unique=True)
    email = Column(String(254), unique=True)

    @classmethod
    def create(cls, session, data):
        name = data["username"]
        email = f"{name}@ramones.org"
        return cls(username=name, email=email)


@pytest.fixture(scope="session")
def engine():
    return create_engine("sqlite://")


@pytest.fixture(scope="session")
def tables(engine):
    BaseModel.metadata.create_all(engine)
    yield
    BaseModel.metadata.drop_all(engine)


@pytest.fixture
def session(engine, tables):
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = Session(bind=connection)

    yield session

    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()

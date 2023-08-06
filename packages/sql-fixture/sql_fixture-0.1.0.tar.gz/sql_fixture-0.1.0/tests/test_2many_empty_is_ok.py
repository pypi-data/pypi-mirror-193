from sql_fixture import fixture
from tests.conftest import BaseModel, Group


def test_2many_empty_is_ok(session):
    fixtures = """
      - User:
        - __key__: joey
          username: joey
          email: joey@example.com
          profile:
            name: Jeffrey

      - Group:
        - name: Ramones
          members: []
    """
    fixture.load(BaseModel, session, fixtures)
    groups = session.query(Group).all()
    assert len(groups) == 1
    assert len(groups[0].members) == 0

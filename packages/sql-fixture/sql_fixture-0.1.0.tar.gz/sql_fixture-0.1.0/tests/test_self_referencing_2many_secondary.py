from sql_fixture import fixture
from tests.conftest import BaseModel, User


def test_self_referencing_2many_secondary(session):
    fixtures = """
- User:
  - __key__: joey
    username: joey
  - __key__: johnny
    username: johnny
  - __key__: tommy
    username: tommy
    email: tommy@example.com
    friends:
      - joey
      - johnny
"""
    fixture.load(BaseModel, session, fixtures)
    users = session.query(User).order_by(User.username).all()
    assert len(users[0].friends) == 0
    assert len(users[1].friends) == 0
    assert len(users[2].friends) == 2
    assert users[2].username == "tommy"
    assert users[2].friends[0].username == "joey"
    assert users[2].friends[1].username == "johnny"

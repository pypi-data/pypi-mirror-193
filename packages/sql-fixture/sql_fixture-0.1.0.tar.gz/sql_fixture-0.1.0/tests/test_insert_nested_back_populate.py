from sql_fixture import fixture
from tests.conftest import BaseModel, User


def test_insert_nested_back_populate(session):
    fixtures = """
- User:
  - username: joey
    email: joey@example.com
    profile2:
      name: Jeffrey
"""
    fixture.load(BaseModel, session, fixtures)
    users = session.query(User).all()
    assert len(users) == 1
    assert users[0].profile2.name == "Jeffrey"

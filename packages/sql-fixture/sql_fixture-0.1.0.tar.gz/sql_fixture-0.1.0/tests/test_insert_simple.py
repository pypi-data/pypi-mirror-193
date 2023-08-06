from sql_fixture import fixture
from tests.conftest import BaseModel, User


def test_insert_simple(session):
    fixtures = """
- User:
  - username: deedee
    email: deedee@example.com
  - username: joey
    email: joey@example.commit
"""
    fixture.load(BaseModel, session, fixtures)
    users = session.query(User).all()
    assert len(users) == 2
    assert users[0].username == "deedee"
    assert users[1].username == "joey"

from sql_fixture import fixture
from tests.conftest import BaseModel, Profile3


def test_insert_nested_NO_back_populate(session):
    fixtures = """
- Profile3:
  - name: Jeffrey
    user:
      username: joey
      email: joey@example.com
"""
    fixture.load(BaseModel, session, fixtures)
    profiles = session.query(Profile3).all()
    assert len(profiles) == 1
    assert profiles[0].name == "Jeffrey"
    assert profiles[0].user.username == "joey"

from sql_fixture import fixture
from tests.conftest import BaseModel, User


def test_init_param_ref(session):
    fixtures = """
- User:
  - __key__: joey
    username: joey
    email: joey@example.com

- Profile:
  - the_user: {ref: joey}
    name: Jeffrey
"""
    fixture.load(BaseModel, session, fixtures)
    users = session.query(User).all()
    assert len(users) == 1
    assert users[0].profile.name == "Jeffrey"

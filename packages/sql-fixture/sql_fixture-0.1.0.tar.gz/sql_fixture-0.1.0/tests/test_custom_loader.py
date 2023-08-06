from sql_fixture import fixture
from tests.conftest import BaseModel, Person


def test_custom_loader(session):
    fixtures = """
- 'Person:create':
  - username: joey
  - username: deedee
"""
    fixture.load(BaseModel, session, fixtures)
    users = session.query(Person).order_by(Person.username).all()
    assert len(users) == 2
    assert users[0].username == "deedee"
    assert users[0].email == "deedee@ramones.org"
    assert users[1].username == "joey"
    assert users[1].email == "joey@ramones.org"

from sql_fixture import fixture
from tests.conftest import BaseModel, User


def test_store_returned(session):
    fixtures = """
- User:
  - __key__: dee
    username: deedee
    email: deedee@example.com
"""
    store = fixture.load(BaseModel, session, fixtures)
    users = session.query(User).all()
    assert len(users) == 1
    assert users[0].username == "deedee"
    assert users[0].id is not None
    assert users[0].id == store.get("dee").id

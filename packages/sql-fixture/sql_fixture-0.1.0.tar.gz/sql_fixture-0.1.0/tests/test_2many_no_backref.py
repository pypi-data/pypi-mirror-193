from sql_fixture import fixture
from tests.conftest import BaseModel, Role


def test_2many_no_backref(session):
    fixtures = """
- User:
  - __key__: joey
    username: joey
    email: joey@example.com
    roles:
      - name: owner
      - name: editor
      - name: viewer
"""
    data = fixture.load(BaseModel, session, fixtures)
    roles = session.query(Role).all()
    assert len(roles) == 3
    assert roles[0].user_id == data.get("joey").id

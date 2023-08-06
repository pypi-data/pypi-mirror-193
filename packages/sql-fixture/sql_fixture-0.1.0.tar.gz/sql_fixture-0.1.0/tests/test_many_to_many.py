from sql_fixture import fixture
from tests.conftest import BaseModel, Group


def test_2many(session):
    fixtures = """
- User:
  - __key__: joey
    username: joey
    email: joey@example.com
    profile:
      name: Jeffrey

- Group:
  - name: Ramones
    members: [joey.profile]
"""
    fixture.load(BaseModel, session, fixtures)
    groups = session.query(Group).all()
    assert len(groups) == 1
    assert groups[0].members[0].profile.name == "Jeffrey"
    assert groups[0].members[0].profile.groups[0].group.name == "Ramones"

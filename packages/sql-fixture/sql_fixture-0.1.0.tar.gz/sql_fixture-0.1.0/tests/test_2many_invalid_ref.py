import pytest

from sql_fixture import fixture
from tests.conftest import BaseModel


def test_2many_invalid_ref(session):
    fixtures = """
- User:
  - __key__: joey
    username: joey
    email: joey@example.com
    profile:
      name: Jeffrey

- Group:
  - name: Ramones
    members: [joey]
"""
    with pytest.raises(Exception) as exc_info:
        fixture.load(BaseModel, session, fixtures)
    assert "Group" in str(exc_info)
    assert "members" in str(exc_info)
    assert "joey" in str(exc_info)

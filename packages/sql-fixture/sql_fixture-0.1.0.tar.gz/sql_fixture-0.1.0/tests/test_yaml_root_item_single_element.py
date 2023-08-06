import pytest

from sql_fixture import fixture
from tests.conftest import BaseModel


def test_yaml_root_item_single_element(session):
    fixtures = """
- User:
  - username: deedee
    email: deedee@example.com
  Group:
  - name: Ramones
"""
    with pytest.raises(Exception) as exc_info:
        fixture.load(BaseModel, session, fixtures)
    assert "Sequence item must contain only one mapper" in str(exc_info)
    assert "Group" in str(exc_info)
    assert "User" in str(exc_info)

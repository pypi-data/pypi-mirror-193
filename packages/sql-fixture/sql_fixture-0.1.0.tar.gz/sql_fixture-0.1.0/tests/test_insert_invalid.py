import pytest

from sql_fixture import fixture
from tests.conftest import BaseModel


def test_insert_invalid(session):
    fixtures = """
- User:
  - username: deedee
    email: deedee@example.com
    color_no: blue
"""
    with pytest.raises(Exception) as exc_info:
        fixture.load(BaseModel, session, fixtures)
    assert "User" in str(exc_info)
    assert "color_no" in str(exc_info)

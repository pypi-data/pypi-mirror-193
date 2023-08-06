import pytest

from sql_fixture import fixture
from tests.conftest import BaseModel


def test_mapper_must_contain_list(session):
    fixtures = """
    - User:
        username: deedee
        email: deedee@example.com
"""
    with pytest.raises(Exception) as exc_info:
        fixture.load(BaseModel, session, fixtures)
    assert "Mapper `User` should have a list of instances." in str(exc_info)
    assert "User" in str(exc_info)

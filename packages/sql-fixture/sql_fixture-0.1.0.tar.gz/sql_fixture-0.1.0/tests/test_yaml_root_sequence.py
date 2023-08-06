import pytest

from sql_fixture import fixture
from tests.conftest import BaseModel


def test_yaml_root_sequence(session):
    fixtures = """
User:
  - username: deedee
    email: deedee@example.com
"""
    with pytest.raises(Exception) as exc_info:
        fixture.load(BaseModel, session, fixtures)
    assert "Top level YAML" in str(exc_info)
    assert "sequence" in str(exc_info)

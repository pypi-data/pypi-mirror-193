from sql_fixture import fixture
from tests.conftest import BaseModel, User


def test_2many_secondary(session):
    fixtures = """
      - Instrument:
        - __key__: drums
          name: drums
        - __key__: guitar
          name: guitar

      - User:
        - __key__: joey
          username: joey
          email: joey@example.com
          instruments:
            - drums
            - guitar
    """
    fixture.load(BaseModel, session, fixtures)
    users = session.query(User).order_by(User.username).all()
    assert users[0].username == "joey"
    assert users[0].instruments[0].name == "drums"
    assert users[0].instruments[1].name == "guitar"

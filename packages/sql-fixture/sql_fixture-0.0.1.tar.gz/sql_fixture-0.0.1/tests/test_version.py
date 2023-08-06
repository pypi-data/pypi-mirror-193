import sql_fixture


def test_version() -> None:
    assert sql_fixture.__version__ == "0.0.1"

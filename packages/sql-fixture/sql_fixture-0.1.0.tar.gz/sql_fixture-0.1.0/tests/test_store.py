import pytest

from sql_fixture import fixture


class TestStore:
    def test_put_get(self):
        self.extracted_key("bar", "foo", "bar")

    def test_get_non_existent(self):
        store = fixture.Store()
        assert pytest.raises(KeyError, store.get, "foo")

    def test_duplicate_key_raises(self):
        store = fixture.Store()
        store.put("foo", "bar")
        assert pytest.raises(AssertionError, store.put, "foo", "second")

    def test_dotted_key(self):
        class Foo:
            bar = 52

        self.extracted_key(Foo, "foo.bar.__class__.__name__", "int")

    def extracted_key(self, arg0, arg1, arg2):
        store = fixture.Store()
        store.put("foo", arg0)
        assert store.get(arg1) == arg2

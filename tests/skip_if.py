import pytest


def skip_if_zope(f):
    def wrapper(self, *args, **kwargs):
        if self.__class__.__name__ == "TestZopeTestBrowserDriver":
            return pytest.skip("skipping this test for zope testbrowser")
        else:
            f(self, *args, **kwargs)

    return wrapper


def skip_if_django(f):
    def wrapper(self, *args, **kwargs):
        if self.__class__.__name__ == "TestDjangoClientDriver":
            return pytest.skip("skipping this test for django")
        else:
            f(self, *args, **kwargs)

    return wrapper


def skip_if_flask(f):
    def wrapper(self, *args, **kwargs):
        if self.__class__.__name__ == "TestFlaskClientDriver":
            return pytest.skip("skipping this test for flask")
        else:
            f(self, *args, **kwargs)

    return wrapper

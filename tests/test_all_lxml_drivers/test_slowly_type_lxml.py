import pytest

from tests.fake_webapp import EXAMPLE_APP


def test_simple_type(browser):
    """
    lxml-based drivers won't support type method
    because it doesn't interact with JavaScript
    """
    browser.visit(EXAMPLE_APP)
    with pytest.raises(NotImplementedError):
        browser.find_by_name("query").type("with type method")


def test_simple_type_on_element(browser):
    """
    lxml-based drivers won't support type method
    because it doesn't interact with JavaScript
    """
    browser.visit(EXAMPLE_APP)
    with pytest.raises(NotImplementedError):
        browser.find_by_name("query").type("with type method")


def test_slowly_typing(browser):
    """
    lxml-based drivers won't support type method
    because it doesn't interact with JavaScript
    """
    browser.visit(EXAMPLE_APP)
    with pytest.raises(NotImplementedError):
        browser.find_by_name("query").type("with type method", slowly=True)


def test_slowly_typing_on_element(browser):
    """
    lxml-based drivers won't support type method
    on element because it doesn't interac with JavaScript
    """
    browser.visit(EXAMPLE_APP)
    with pytest.raises(NotImplementedError):
        query = browser.find_by_name("query")
        query.type("with type method", slowly=True)

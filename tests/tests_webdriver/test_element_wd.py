from selenium.common.exceptions import WebDriverException

import pytest

from tests.fake_webapp import EXAMPLE_APP


def test_can_see_the_text_for_an_element(browser):
    "should provide text for an element"
    browser.visit(EXAMPLE_APP)
    assert browser.find_by_id("simple_text").text == "my test text"


def test_the_text_for_an_element_strips_html_tags(browser):
    "should show that the text attribute strips html"
    browser.visit(EXAMPLE_APP)
    assert browser.find_by_id("text_with_html").text == "another bit of text"


def test_can_verify_if_a_element_is_visible(browser):
    "should provide verify if element is visible"
    browser.visit(EXAMPLE_APP)
    assert browser.find_by_id("visible").visible


def test_can_verify_if_a_element_is_invisible(browser):
    "should provide verify if element is invisible"
    browser.visit(EXAMPLE_APP)
    assert not browser.find_by_id("invisible").visible


def test_can_select_a_option_via_element_text(browser):
    "should provide a way to select a option via element"
    browser.visit(EXAMPLE_APP)
    assert not browser.find_option_by_value("rj").selected
    browser.find_by_name("uf").select_by_text("Rio de Janeiro")
    assert browser.find_option_by_value("rj").selected


def test_click_intercepted(browser):
    """Intercepted clicks should retry."""
    browser.visit(EXAMPLE_APP + "click_intercepted")
    browser.wait_time = 10
    # Clicking this element adds a new element to the page.
    browser.find_by_id("overlapped").click()
    value = browser.find_by_id("added_container").value
    assert "Added" == value
    browser.wait_time = 2


def test_click_intercepted_fails(browser):
    """Intercepted clicks that never unblock should raise an error."""
    browser.visit(EXAMPLE_APP + "click_intercepted")

    with pytest.raises(WebDriverException):
        browser.find_by_id("overlapped2").click()

# Copyright 2012 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import os
import re
import time

import pytest

from splinter.exceptions import ElementDoesNotExist

from tests.fake_webapp import EXAMPLE_APP


skip_if_zope = pytest.mark.skipif(
    os.getenv("ZOPE"),
    reason="Test not compatible with zope.testbrowser",
)

skip_if_safari = pytest.mark.skipif(
    os.getenv("SAFARI"),
    reason="Test not compatible with safari",
)


def test_fill(browser):
    browser.visit(EXAMPLE_APP)
    my_input = "LT-CS-01/2018"
    elem = browser.find_by_name("query")
    elem.fill(my_input)
    assert my_input == elem.value


def test_fill_element(browser):
    browser.visit(EXAMPLE_APP)
    browser.find_by_name("q").fill("new query")
    time.sleep(1)
    value = browser.find_by_name("q").value
    assert "new query" == value


@skip_if_zope
@skip_if_safari
def test_clicking_submit_input_doesnt_post_input_value_if_name_not_present(browser):
    browser.visit(EXAMPLE_APP)
    browser.find_by_css("input.submit-input-no-name").click()
    elem = browser.find_by_xpath("/descendant-or-self::*")
    assert elem.text.strip() == ""


@skip_if_zope
@skip_if_safari
def test_clicking_submit_input_posts_empty_value_if_value_not_present(browser):
    browser.visit(EXAMPLE_APP)
    browser.find_by_css('input[name="submit-input-no-value"]').click()
    body_text = browser.find_by_xpath("/descendant-or-self::*").text.strip()
    assert re.match(r"^submit-input-no-value:(?:| Submit| Submit Query)$", body_text), repr(body_text)


@skip_if_zope
@skip_if_safari
def test_clicking_submit_input_doesnt_post_input_value_if_empty(browser):
    browser.visit(EXAMPLE_APP)
    browser.find_by_css("input.submit-input-empty").click()
    elem = browser.find_by_xpath("/descendant-or-self::*")
    assert elem.text.strip() == ""


@skip_if_safari
def test_clicking_submit_input_posts_input_value_if_value_present(browser):
    browser.visit(EXAMPLE_APP)
    browser.find_by_css('input[name="submit-input"]').click()
    elem = browser.find_by_xpath("/descendant-or-self::*")
    assert elem.text == "submit-input: submit-input-value"


@skip_if_zope
@skip_if_safari
def test_clicking_submit_button_doesnt_post_button_value_if_name_not_present(browser):
    browser.visit(EXAMPLE_APP)
    browser.find_by_css("button.submit-button-no-name").click()
    elem = browser.find_by_xpath("/descendant-or-self::*")
    assert elem.text == ""


@skip_if_zope
def test_clicking_submit_button_posts_empty_value_if_value_not_present(browser):
    browser.visit(EXAMPLE_APP)
    browser.find_by_css('button[name="submit-button-no-value"]').click()
    assert browser.find_by_xpath("/descendant-or-self::*").text.strip() == "submit-button-no-value:"


@skip_if_zope
@skip_if_safari
def test_clicking_submit_button_doesnt_post_button_value_if_empty(browser):
    browser.visit(EXAMPLE_APP)
    browser.find_by_css("button.submit-button-empty").click()
    assert browser.find_by_xpath("/descendant-or-self::*").text.strip() == ""


@skip_if_zope
def test_clicking_submit_button_posts_button_value_if_value_present(browser):
    browser.visit(EXAMPLE_APP)
    browser.find_by_css('button[name="submit-button"]').click()

    assert browser.find_by_xpath("/descendant-or-self::*").text == "submit-button: submit-button-value"


@skip_if_safari
def test_submiting_a_form_and_verifying_page_content(browser):
    browser.visit(EXAMPLE_APP)
    browser.find_by_name("query").fill("my name")
    browser.find_by_name("send").click()
    assert "My name is: Master Splinter" in browser.html


def test_can_choose_a_radio_button(browser):
    "should provide a way to choose a radio button"
    browser.visit(EXAMPLE_APP)
    assert not browser.find_by_id("gender-m").checked
    browser.choose("gender", "M")
    assert browser.find_by_id("gender-m").checked


def test_can_find_textarea_by_tag(browser):
    "should provide a way to find a textarea by tag_name"
    browser.visit(EXAMPLE_APP)
    tag = browser.find_by_tag("textarea").first
    assert "" == tag.value


def test_can_find_input_without_type(browser):
    "should recognize an input element that doesn't have a `type` attribute"
    browser.visit(EXAMPLE_APP)
    tag = browser.find_by_css('[name="typeless"]').first
    assert "default value" == tag.value


def test_can_find_button(browser):
    "should recognize a button"
    browser.visit(EXAMPLE_APP)
    tag = browser.find_by_css(".just-a-button").first
    assert hasattr(tag, "click")


def test_can_find_option_by_value(browser):
    "should provide a way to find select option by value"
    browser.visit(EXAMPLE_APP)
    assert "Rio de Janeiro" == browser.find_option_by_value("rj").text


def test_can_get_value_attribute_for_a_option(browser):
    "should option have a value attribute"
    browser.visit(EXAMPLE_APP)
    assert "rj" == browser.find_option_by_value("rj")["value"]


def test_can_find_option_by_text(browser):
    "should provide a way to find select option by text"
    browser.visit(EXAMPLE_APP)
    assert "rj" == browser.find_option_by_text("Rio de Janeiro").value


def test_can_select_a_option(browser):
    "should provide a way to select a option"
    browser.visit(EXAMPLE_APP)
    assert not browser.find_option_by_value("rj").selected
    browser.select("uf", "rj")
    assert browser.find_option_by_value("rj").selected


def test_can_select_an_option_in_an_optgroup(browser):
    "should provide a way to select an option that is in an optgroup"
    browser.visit(EXAMPLE_APP)
    assert browser.find_by_name("food").value == "apples"
    browser.select("food", "grapes")
    assert browser.find_by_name("food").value == "grapes"


def test_can_select_a_option_via_element(browser):
    "should provide a way to select a option via element"
    browser.visit(EXAMPLE_APP)
    assert not browser.find_option_by_value("rj").selected
    browser.find_by_name("uf").select("rj")
    assert browser.find_option_by_value("rj").selected


def test_can_check_a_checkbox(browser):
    """should provide a way to check a radio checkbox"""
    browser.visit(EXAMPLE_APP)
    elem = browser.find_by_name("some-check")
    assert not elem.checked
    elem.check()
    assert elem.checked


def test_check_keeps_checked_if_called_multiple_times(browser):
    """should keep a checkbox checked if check() is called multiple times"""
    browser.visit(EXAMPLE_APP)
    elem = browser.find_by_name("some-check")
    assert not elem.checked
    elem.check()
    elem.check()
    assert elem.checked


def test_can_uncheck_a_checkbox(browser):
    """should provide a way to uncheck a radio checkbox"""
    browser.visit(EXAMPLE_APP)
    elem = browser.find_by_name("checked-checkbox")
    assert elem.checked
    elem.uncheck()
    assert not elem.checked


def test_uncheck_should_keep_unchecked_if_called_multiple_times(browser):
    """should keep a checkbox unchecked if uncheck() is called multiple times"""
    browser.visit(EXAMPLE_APP)
    elem = browser.find_by_name("checked-checkbox")
    assert elem.checked
    elem.uncheck()
    elem.uncheck()
    assert not elem.checked


def test_can_fill_text_field_in_form(browser):
    "should provide a away to change field value"
    browser.visit(EXAMPLE_APP)
    browser.fill_form({"query": "new query"})
    value = browser.find_by_name("query").value
    assert "new query" == value


def test_can_fill_password_field_in_form(browser):
    "should provide a way to change password value"
    browser.visit(EXAMPLE_APP)
    new_password = "new password"
    browser.fill_form({"password": new_password})
    value = browser.find_by_name("password").value
    assert new_password == value


@skip_if_safari
def test_can_fill_more_than_one_field_in_form(browser):
    "should provide a away to change field value"
    browser.visit(EXAMPLE_APP)
    browser.find_by_name("query").fill("my name")
    assert not browser.find_by_id("gender-m").checked
    assert not browser.find_option_by_value("rj").selected
    assert not browser.find_by_name("some-check").checked
    assert browser.find_by_name("checked-checkbox").checked
    browser.fill_form(
        {
            "query": "another new query",
            "description": "Just another description value in the textarea",
            "gender": "M",
            "uf": "rj",
            "some-check": True,
            "checked-checkbox": False,
        },
    )
    query_value = browser.find_by_name("query").value
    assert "another new query" == query_value
    desc_value = browser.find_by_name("description").value
    assert "Just another description value in the textarea" == desc_value
    assert browser.find_by_id("gender-m").checked
    assert browser.find_option_by_value("rj").selected
    assert browser.find_by_name("some-check").checked
    assert not browser.find_by_name("checked-checkbox").checked


def test_can_fill_tel_text_field(browser):
    "should provide a way to change a tel field value"
    browser.visit(EXAMPLE_APP)
    new_telephone = "555-0042"
    browser.fill_form({"telephone": new_telephone})
    value = browser.find_by_name("telephone").value
    assert new_telephone == value


def test_can_fill_unknown_text_field(browser):
    "should provide a way to change a unknown text field type that isn't specifically defined"
    browser.visit(EXAMPLE_APP)
    new_search_keyword = "foobar"
    browser.fill_form({"search_keyword": new_search_keyword})
    value = browser.find_by_name("search_keyword").value
    assert new_search_keyword == value


def test_can_fill_form_by_id(browser):
    "should be able to fill a form by its id"
    browser.visit(EXAMPLE_APP)
    browser.fill_form(
        {"firstname": "John", "lastname": "Doe"},
        form_id="login",
    )
    value = browser.find_by_name("firstname").value
    assert "John" == value


@skip_if_zope
def test_fill_form_missing_values(browser):
    """Missing values should raise an error."""
    browser.visit(EXAMPLE_APP)
    with pytest.raises(ElementDoesNotExist) as e:
        browser.fill_form(
            {"query": "new query", "missing_form": "doesn't exist"},
        )

    assert "missing_form" in str(e.value)


def test_fill_form_missing_values_ignore_missing(browser):
    """Missing values are ignores when ignore_missing is True."""
    browser.visit(EXAMPLE_APP)
    browser.fill_form(
        {"query": "new query", "missing_form": "doesn't exist"},
        ignore_missing=True,
    )
    value = browser.find_by_name("query").value
    assert "new query" == value

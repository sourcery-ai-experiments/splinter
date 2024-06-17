# Copyright 2012 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from tests.fake_webapp import EXAMPLE_APP


def test_is_text_present(browser):
    "should verify if text is present"
    browser.visit(EXAMPLE_APP)
    assert browser.is_text_present("Example Header")


def test_is_text_present_and_should_return_false(browser):
    "should verify if text is present and return false"
    browser.visit(EXAMPLE_APP)
    assert not browser.is_text_present("Text that not exist")


def test_is_text_present_and_should_wait_time(browser):
    "should verify if text is present and wait for five seconds"
    browser.visit(EXAMPLE_APP)
    browser.links.find_by_text("FOO").click()
    assert browser.is_text_present("BAR!", wait_time=20)


def test_is_text_not_present(browser):
    "should verify if text is not present"
    browser.visit(EXAMPLE_APP)
    assert browser.is_text_not_present("Text that not exist")


def test_is_text_not_present_and_should_return_false(browser):
    "should verify if text is not present and return false"
    browser.visit(EXAMPLE_APP)
    assert not browser.is_text_not_present("Example Header")


def test_is_text_not_present_and_should_wait_time(browser):
    "should verify if text is not present and wait for five seconds"
    browser.visit(EXAMPLE_APP)
    browser.links.find_by_text("FOO").click()
    assert browser.is_text_not_present("another text", wait_time=20)


def test_is_text_present_no_body(browser):
    "should work properly (return false) even if there's no body"
    browser.visit(EXAMPLE_APP + "no-body")
    assert not browser.is_text_present("No such text")


def test_is_text_not_present_no_body(browser):
    "returns true if there's no body"
    browser.visit(EXAMPLE_APP + "no-body")
    assert browser.is_text_not_present("No such text")

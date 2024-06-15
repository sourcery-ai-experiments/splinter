# Copyright 2014 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import pytest


from tests.fake_webapp import app
from tests.fake_webapp import EXAMPLE_APP


@pytest.fixture()
def browser_kwargs():
    return {"app": app, "wait_time": 0.1}


def test_serialize_select_mutiple(browser):
    """should serialize a select with multiple values into a list"""
    browser.visit(EXAMPLE_APP)
    browser.select("pets", ["cat", "dog"])
    form = browser.find_by_name("send")._get_parent_form()
    data = browser.serialize(form)
    assert data["pets"] == ["cat", "dog"]


def test_redirection_on_post(browser):
    """
    when submitting a form that POSTs to /redirected,
    browser should be redirected to GET /redirected-location?come=get&some=true
    """
    browser.visit(EXAMPLE_APP)
    browser.find_by_name("redirect").click()
    assert "I just been redirected to this location" in browser.html
    assert "redirect-location?come=get&some=true" in browser.url

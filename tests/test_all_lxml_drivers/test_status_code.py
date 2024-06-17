# Copyright 2012 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from tests.fake_webapp import EXAMPLE_APP

import pytest


@pytest.mark.xfail(reason="str() of status_code returns unexpected string.")
def test_should_visit_index_of_example_app_and_get_200_status_code(browser):
    browser.visit(EXAMPLE_APP)
    assert 200 == browser.status_code
    assert "200 - OK" == str(browser.status_code)


@pytest.mark.xfail(reason="str() of status_code returns unexpected string.")
def test_should_visit_error_of_example_app_and_not_get_200_status_code(browser):
    browser.visit(EXAMPLE_APP + "error.html")
    assert 200 != browser.status_code
    assert "404 - Not Found" == str(browser.status_code)

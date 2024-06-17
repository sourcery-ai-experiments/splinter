# Copyright 2013 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import pytest

from tests.fake_webapp import EXAMPLE_APP


def test_fill_form_missing_values(browser):
    """Missing values should raise an error."""
    browser.visit(EXAMPLE_APP)
    with pytest.raises(LookupError):
        browser.fill_form(
            {"query": "new query", "missing_form": "doesn't exist"},
        )

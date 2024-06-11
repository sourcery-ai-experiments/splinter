# Copyright 2013 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import pytest

from .base import get_browser
from .base import WebDriverTests
from .keyboard import KeyboardTest
from .fake_webapp import EXAMPLE_APP

from splinter.config import Config


class TestChromeBrowser(WebDriverTests, KeyboardTest):
    @pytest.fixture(autouse=True, scope="class")
    def setup_browser(self, request):
        config = Config(fullscreen=False)
        request.cls.browser = get_browser("chrome", config=config)
        request.addfinalizer(request.cls.browser.quit)

    @pytest.fixture(autouse=True)
    def visit_example_app(self, request):
        self.browser.driver.set_window_size(1024, 768)
        self.browser.visit(EXAMPLE_APP)


class TestChromeBrowserFullscreen(WebDriverTests, KeyboardTest):
    @pytest.fixture(autouse=True, scope="class")
    def setup_browser(self, request):
        config = Config(fullscreen=True)
        request.cls.browser = get_browser("chrome", config=config)
        request.addfinalizer(request.cls.browser.quit)

    @pytest.fixture(autouse=True)
    def visit_example_app(self):
        self.browser.visit(EXAMPLE_APP)

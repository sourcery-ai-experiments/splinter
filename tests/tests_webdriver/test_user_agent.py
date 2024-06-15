import os

import pytest

from splinter.config import Config

from tests.fake_webapp import EXAMPLE_APP


IS_REMOTE_WEBDRIVER = os.getenv("REMOTE_WEBDRIVER")


@pytest.fixture(scope="session")
def browser_config():
    return Config(user_agent="iphone", headless=True)


@pytest.mark.skipif(IS_REMOTE_WEBDRIVER, reason="No compatible with remote webdriver")
def test_should_be_able_to_change_user_agent(browser):
    browser.visit(EXAMPLE_APP + "useragent")

    assert "iphone" in browser.html

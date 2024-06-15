import os
import pathlib

import pytest

from tests.fake_webapp import EXAMPLE_APP


xfail_if_safari = pytest.mark.xfail(
    os.getenv("SAFARI"),
    reason="Session issues with safari need to be investigated.",
)


def test_default_wait_time(browser):
    "should driver default wait time 2"
    assert 2 == browser.wait_time


def test_status_code(browser):
    with pytest.raises(NotImplementedError):
        browser.status_code


def test_can_open_page_in_new_tab(browser):
    """should be able to visit url in a new tab"""
    browser.visit(EXAMPLE_APP)
    browser.windows.current.new_tab(EXAMPLE_APP)
    browser.windows[1].is_current = True
    assert EXAMPLE_APP == browser.url
    assert 2 == len(browser.windows)

    browser.windows[0].is_current = True
    browser.windows[1].close()


def test_attach_file(request, browser):
    """Should provide a way to change file field value"""
    file_path = pathlib.Path(
        os.getcwd(),  # NOQA PTH109
        "tests",
        "mockfile.txt",
    )

    browser.visit(EXAMPLE_APP)
    browser.attach_file("file", str(file_path))
    browser.find_by_name("upload").click()

    html = browser.html
    assert "text/plain" in html

    with open(file_path) as f:
        assert str(f.read()) in html


@xfail_if_safari
def test_browser_config(request, browser_name):
    """Splinter's drivers get the Config object when it's passed through the Browser function."""
    from splinter import Config
    from splinter import Browser

    config = Config(user_agent="agent_smith", headless=True)
    browser = Browser(browser_name, config=config)
    request.addfinalizer(browser.quit)

    assert browser.config.user_agent == "agent_smith"

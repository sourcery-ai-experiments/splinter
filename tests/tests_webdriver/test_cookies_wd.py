import time

from tests.fake_webapp import EXAMPLE_APP


def test_cookies_extra_parameters(browser):
    """Cookie can be created with extra parameters."""
    browser.visit(EXAMPLE_APP)
    timestamp = int(time.time() + 120)
    browser.cookies.add({"sha": "zam"}, expiry=timestamp)
    cookie = browser.driver.get_cookie("sha")
    assert timestamp == cookie["expiry"]

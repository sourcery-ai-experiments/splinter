from .fake_webapp import EXAMPLE_APP


def test_cookies_extra_parameters(browser):
    """Cookie can be created with extra parameters."""
    browser.visit(EXAMPLE_APP)
    comment = "Ipsum lorem"
    browser.cookies.add({"sha": "zam"}, comment=comment)
    cookie = browser._browser.cookies.getinfo("sha")
    assert "Ipsum%20lorem" == cookie["comment"]

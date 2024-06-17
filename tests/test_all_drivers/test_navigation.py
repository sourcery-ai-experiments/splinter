from tests.fake_webapp import EXAMPLE_APP


def test_can_open_page(browser):
    """should be able to visit, get title and quit"""
    browser.visit(EXAMPLE_APP)
    assert "Example Title" == browser.title


def test_should_reload_a_page(browser):
    browser.visit(EXAMPLE_APP)
    browser.reload()
    assert "Example Title" == browser.title


def test_can_back_on_history(browser):
    """should be able to back on history"""
    browser.visit(EXAMPLE_APP)
    browser.visit(f"{EXAMPLE_APP}iframe")
    browser.back()
    assert EXAMPLE_APP == browser.url


def test_can_forward_on_history(request, browser):
    """User can forward history"""
    request.addfinalizer(browser.quit)

    next_url = f"{EXAMPLE_APP}iframe"

    browser.visit(EXAMPLE_APP)
    browser.visit(next_url)
    browser.back()

    browser.forward()
    assert next_url == browser.url


def test_redirection(browser):
    """
    when visiting /redirected, browser should be redirected to /redirected-location?come=get&some=true
    browser.url should be updated
    """
    browser.visit(f"{EXAMPLE_APP}redirected")
    assert "I just been redirected to this location." in browser.html
    assert "redirect-location?come=get&some=true" in browser.url

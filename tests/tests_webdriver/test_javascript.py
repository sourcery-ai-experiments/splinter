from tests.fake_webapp import EXAMPLE_APP


def test_can_execute_javascript(browser):
    "should be able to execute javascript"
    browser.visit(EXAMPLE_APP)
    browser.execute_script("$('body').empty()")
    assert "" == browser.find_by_tag("body").value


def test_can_evaluate_script(browser):
    "should evaluate script"
    assert 8 == browser.evaluate_script("4+4")


def test_execute_script_returns_result_if_present(browser):
    assert browser.execute_script("return 42") == 42

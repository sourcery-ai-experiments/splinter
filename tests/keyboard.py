from splinter.driver.webdriver import Keyboard


class KeyboardTest:
    def test_keyboard_down_modifier(self):
        keyboard = Keyboard(self.browser.driver)

        keyboard.down("CONTROL")

        elem = self.browser.find_by_css("#keypress_detect")

        assert elem.first

    def test_keyboard_up_modifier(self):
        keyboard = Keyboard(self.browser.driver)

        keyboard.down("CONTROL")
        keyboard.up("CONTROL")

        elem = self.browser.find_by_css("#keyup_detect")

        assert elem.first

    def test_keyboard_press_modifier(self):
        keyboard = Keyboard(self.browser.driver)

        keyboard.press("CONTROL")

        elem = self.browser.find_by_css("#keyup_detect")

        assert elem.first

    def test_element_press_combo(self):
        keyboard = Keyboard(self.browser.driver)

        keyboard.press("CONTROL+a")

        elem = self.browser.find_by_css("#keypress_detect_a")

        assert elem.first

# Copyright 2012 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from .skip_if import skip_if_zope, skip_if_django, skip_if_flask


class ElementTest:
    def test_element_has_class_when_element_has_the_class_as_first_class(self):
        assert self.browser.find_by_css(".has-class-first").has_class("has-class-first")

    def test_element_has_class_when_element_has_the_class_as_middle_class(self):
        assert self.browser.find_by_css(".has-class-middle").has_class("has-class-middle")

    def test_element_has_class_when_element_has_the_class_as_end_class(self):
        assert self.browser.find_by_css(".has-class-end").has_class("has-class-end")

    def test_element_has_class_when_element_doesnt_have_the_class(self):
        assert not self.browser.find_by_css(".has-class-first").has_class("has-class")

    def test_element_outer_html(self):
        assert self.browser.find_by_id("html-property").outer_html == (
            '<div id="html-property" class="outer html classes">'
            'inner <div class="inner-html">inner text</div> html test</div>'
        )

    def test_element_html_with_breakline(self):
        assert self.browser.find_by_id("html-property-with-breakline").html == "\\n     some text here\\n"

    def test_element_html(self):
        assert (
            self.browser.find_by_id("html-property").html == 'inner <div class="inner-html">inner text</div> html test'
        )

    @skip_if_zope
    @skip_if_django
    @skip_if_flask
    def test_element_press_modifier(self):
        elem = self.browser.find_by_css("[name='q']")
        elem.fill("hellox")
        elem.press("BACKSPACE")

        assert elem.value == "hello"

    @skip_if_zope
    @skip_if_django
    @skip_if_flask
    def test_element_press_key(self):
        elem = self.browser.find_by_css("[name='q']")
        elem.fill("hellox")
        elem.press("a")

        assert elem.value == "helloxa"

    @skip_if_zope
    @skip_if_django
    @skip_if_flask
    def test_element_press_combo(self):
        elem = self.browser.find_by_css("[name='q']")
        elem.press("SHIFT+a+BACKSPACE+b")

        assert elem.value == "B"

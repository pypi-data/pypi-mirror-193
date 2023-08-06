from playwright.sync_api import expect
from robotlibcore import keyword
from .utils import random_number_chars
from .ui_context import UIContext
from .utils import Robot


class TextboxHandler(UIContext):

    @keyword('input into')
    def input_into(self, locator, text, clear=True, force=False):
        element = self.get_element(locator)
        if clear:
            element.fill('', force=force)
        element.fill(text, force=force)
        return text

    @keyword('input new text into', tags=["deprecated"])
    def input_new_text_into(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        element.fill(text)

    @keyword("input text by pressing key")
    def input_text_by_pressing_key(self, locator, text, delay=100):
        self.get_element(locator).type(text, delay=delay)
        return text

    @keyword('clear text using backspace')
    def clear_text_using_backspace(self, locator):
        element = self.get_element(locator)
        element.select_text()
        element.press("Backspace")

    @keyword('clear text')
    def clear_text(self, locator):
        self.get_element(locator).fill("")

    @keyword('maxlength should be')
    def maxlength_should_be(self, locator, expected_maxlength):
        element = self.get_element(locator)
        element.fill("")
        length = int(expected_maxlength) + 1
        string = random_number_chars(length)
        element.fill(string)
        Robot().should_be_equal_as_integers(len(element.input_value()), expected_maxlength)
        element.fill("")

    @keyword('textbox should be empty')
    def textbox_should_be_empty(self, locator):
        expect(self.get_element(locator)).to_have_value("")

    @keyword('Placeholder should be')
    def placeholder_should_be(self, locator, expected_text):
        expect(self.get_element(locator)).to_have_attribute("placeholder", expected_text)

    @keyword('textbox should be correct')
    def textbox_should_be_correct(self, locator, state='enabled', default="", mandatory=None, maxlength=None, is_numeric=False):
        element = self.get_element(locator)
        default = default.replace(',', '') if is_numeric else default
        # Verify state
        if state == 'enabled':
            expect(element).to_be_enabled()
        elif state == 'disabled':
            expect(element).to_be_disabled()
        # Verify default value
        if default != "":
            expect(element).to_have_value(default)
        # Verify Max-length
        if maxlength is not None:
            self.maxlength_should_be(element, maxlength)
        # Verify mandatory
        if mandatory == 'unrequired':
            self.element_should_not_be_marked_as_required(element)
        elif mandatory == 'required':
            self.element_should_be_marked_as_required(element)

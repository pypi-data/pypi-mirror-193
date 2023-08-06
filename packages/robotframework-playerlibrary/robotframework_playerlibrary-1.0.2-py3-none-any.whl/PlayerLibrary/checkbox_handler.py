from playwright.sync_api import expect
from robotlibcore import keyword
from .ui_context import UIContext
from .base_context import BaseContext


class CheckboxHandler(UIContext):

    @keyword('checkbox should be enabled')
    def checkbox_should_be_enabled(self, locator):
        element = self.get_element(locator)
        expect(element).to_be_enabled(timeout=BaseContext.SMALL_TIMEOUT)

    @keyword('checkbox should be disabled')
    def checkbox_should_be_disabled(self, locator):
        element = self.get_element(locator)
        expect(element).to_be_disabled(timeout=BaseContext.SMALL_TIMEOUT)

    @keyword('tick checkbox')
    def tick_checkbox(self, locator):
        element = self.get_element(locator)
        element.check()

    @keyword('untick checkbox')
    def untick_checkbox(self, locator):
        element = self.get_element(locator)
        element.uncheck()

    @keyword('checkbox should be checked')
    def checkbox_should_be_checked(self, locator):
        expect(self.get_element(locator)).to_be_checked()

    @keyword('checkbox should not be checked')
    def checkbox_should_not_be_checked(self, locator):
        expect(self.get_element(locator)).not_to_be_checked()

    @keyword('get current checkbox checking status')
    def get_current_checkbox_checking_status(self, locator):
        return self.get_element(locator).is_checked()

    @keyword('checkbox should be correct')
    def checkbox_should_be_correct(self, locator, state='enabled', status='unchecked'):
        element = self.get_element(locator)
        # Verify state
        if state == 'enabled':
            self.checkbox_should_be_enabled(element)
        elif state == 'disabled':
            self.checkbox_should_be_disabled(element)
        # Verify status:
        if status == 'unchecked':
            self.checkbox_should_not_be_checked(element)
        elif status == 'checked':
            self.checkbox_should_be_checked(element)

    @keyword('select a radio option')
    def select_a_radio_option(self, locator):
        self.get_element(locator).check(force=True)

    @keyword('radio button should be disabled')
    def radio_button_should_be_disabled(self, locator):
        expect(self.get_element(locator)).to_be_disabled()

    @keyword('radio button should be enabled')
    def radio_button_should_be_enabled(self, locator):
        expect(self.get_element(locator)).to_be_enabled()

    @keyword('radio button should be checked')
    def radio_button_should_be_checked(self, locator):
        expect(self.get_element(locator)).to_be_checked()

    @keyword('radio button should not be checked')
    def radio_button_should_not_be_checked(self, locator):
        expect(self.get_element(locator)).not_to_be_checked()

    @keyword('get current radio button checking status')
    def get_current_radio_button_checking_status(self, locator):
        return self.get_element(locator).is_checked()

    @keyword('radio should be correct')
    def radio_should_be_correct(self, locator, state='enabled', status='unchecked'):
        element = self.get_element(locator)
        if state == 'enabled':
            self.checkbox_should_be_enabled(element)
        elif state == 'disabled':
            self.checkbox_should_be_disabled(element)
        if status == 'unchecked':
            self.radio_button_should_not_be_checked(element)
        elif status == 'checked':
            self.radio_button_should_be_checked(element)

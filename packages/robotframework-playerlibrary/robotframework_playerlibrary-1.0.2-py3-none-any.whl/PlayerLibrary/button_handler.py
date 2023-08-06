from playwright.sync_api import expect
from robotlibcore import keyword
from .ui_context import UIContext
from .base_context import BaseContext


class ButtonHandler(UIContext):

    @keyword('button should be enabled')
    def button_should_be_enabled(self, locator):
        element = self.get_element(locator)
        expect(element).to_be_enabled(timeout=BaseContext.SMALL_TIMEOUT)

    @keyword('button should be disabled')
    def button_should_be_disabled(self, locator):
        element = self.get_element(locator)
        expect(element).to_be_disabled(timeout=BaseContext.SMALL_TIMEOUT)

    @keyword('button should be correct')
    def button_should_be_correct(self, locator, state='enabled'):
        element = self.get_element(locator)
        self.button_should_be_enabled(element) if state == 'enabled' else self.button_should_be_disabled(element)

    @keyword('click button')
    def click_button(self, locator, force=False):
        element = self.get_element(locator)
        element.click(force=force)

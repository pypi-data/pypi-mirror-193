from playwright.sync_api import expect
from robotlibcore import keyword
from .ui_context import UIContext
from .base_context import BaseContext


class IframeHandler(UIContext):

    @keyword('select iframe')
    def select_iframe(self, locator):
        self.iframe = self.get_page().frame_locator(locator)

    @keyword('unselect iframe')
    def unselect_iframe(self):
        self.iframe = None

    @keyword('iframe should contain')
    def iframe_should_contain(self, *texts, timeout=BaseContext.TIMEOUT):
        for text in texts:
            element = self.iframe.locator(f'//body//*[not(self::script)][contains(text(),"{text}")]')
            expect(element).to_be_visible(timeout=timeout)

    @keyword('iframe should not contain')
    def iframe_should_not_contain(self, *texts, timeout=BaseContext.TIMEOUT):
        for text in texts:
            element = self.iframe.locator(f'//body//*[not(self::script)][contains(text(),"{text}")]')
            expect(element).to_be_hidden(timeout=timeout)

    @keyword('input on iframe')
    def input_on_iframe(self, locator, text):
        self.iframe.locator(locator).fill(text)

    @keyword('click on iframe')
    def click_on_iframe(self, locator):
        self.iframe.locator(locator).click()

    @keyword('tick on iframe')
    def tick_on_iframe(self, locator):
        self.iframe.locator(locator).check()

    @keyword('untick on iframe')
    def untick_on_iframe(self, locator):
        self.iframe.locator(locator).uncheck()

    @keyword('select value on iframe')
    def select_value_on_iframe(self, locator, value):
        self.iframe.locator(locator).select_option(label=value)

    @keyword('iframe should have element')
    def iframe_should_have_element(self, locator):
        expect(self.iframe.locator(locator)).to_be_visible()

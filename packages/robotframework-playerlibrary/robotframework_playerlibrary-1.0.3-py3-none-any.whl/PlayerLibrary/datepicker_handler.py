from datetime import datetime
from playwright.sync_api import expect
from robotlibcore import keyword
from .ui_context import UIContext
from .utils import Robot
from .base_context import BaseContext


class DatePickerHandler(UIContext):

    BASIC_DATE_FORMAT = "%Y-%m-%d"
    ALTERNATIVE_DATE_FORMAT = "%d %b, %Y"

    @keyword('input datetime')
    def input_datetime(self, locator, value):
        element = self.get_element(locator)
        element.evaluate("node => node.removeAttribute('readonly')")
        element.fill(value, force=True)
        self.get_element("xpath=//body").click()
        Robot().sleep(1)
        return value

    @keyword('datepicker should be correct')
    def datepicker_should_be_correct(self, locator, state='enabled', default=None, mandatory=None):
        element = self.get_element(locator)
        # Verify state
        if state == 'enabled':
            expect(element).to_be_enabled()
        elif state == 'disabled':
            expect(element).to_be_disabled()
        # Verify default value
        if default is not None:
            expect(element).to_have_value(default)
        # Verify mandatory
        if mandatory == 'unrequired':
            self.element_should_not_be_marked_as_required(locator)
        elif mandatory == 'required':
            self.element_should_be_marked_as_required(locator)

    @keyword('actual date should be')
    def actual_date_should_be(self, locator, expected_date, input_format=BASIC_DATE_FORMAT,
                              displayed_format=ALTERNATIVE_DATE_FORMAT, timeout=BaseContext.SMALL_TIMEOUT):
        actual_date = None
        for sec in range(int(timeout/1000)):
            actual_date = self.get_actual_text(locator)
            if datetime.strptime(expected_date, input_format) == datetime.strptime(actual_date, displayed_format):
                break
            Robot().sleep(1)
        if datetime.strptime(expected_date, input_format) != datetime.strptime(actual_date, displayed_format):
            raise AssertionError(f"Actual date: '{actual_date}' is different with expected date: '{expected_date}'")

    @keyword('actual date should not be')
    def actual_date_should_not_be(self, locator, expected_date, input_format=BASIC_DATE_FORMAT,
                                  displayed_format=ALTERNATIVE_DATE_FORMAT, timeout=BaseContext.SMALL_TIMEOUT):
        actual_date = None
        for sec in range(int(timeout/1000)):
            actual_date = self.get_actual_text(locator)
            if datetime.strptime(expected_date, input_format) != datetime.strptime(actual_date, displayed_format):
                break
            Robot().sleep(1)
        if datetime.strptime(expected_date, input_format) == datetime.strptime(actual_date, displayed_format):
            raise AssertionError(f"Actual date: '{actual_date}' is similar with expected text: '{expected_date}'")

    @keyword("element is datepicker", tags=["deprecated", "specific"])
    def element_is_datepicker(self, locator):
        return True if self.get_element(locator).get_attribute(locator, "uib-datepicker-popup") is not None else False

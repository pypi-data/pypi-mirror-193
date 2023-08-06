import re
from playwright.sync_api import expect
from robotlibcore import keyword
from .ui_context import UIContext
from .utils import Robot


class DropdownHandler(UIContext):

    @keyword('dropdown should be enabled')
    def dropdown_should_be_enabled(self, locator):
        expect(self.get_element(locator)).to_be_enabled()

    @keyword('dropdown should be disabled')
    def dropdown_should_be_disabled(self, locator):
        expect(self.get_element(locator)).to_be_disabled()

    @keyword('dropdown should be required', tags=['specific'])
    def dropdown_should_be_required(self, locator):
        element = self.get_element(locator).locator("xpath=./preceding-sibling::*")
        expect(element).to_have_class(re.compile(r"required"))

    @keyword('dropdown should not be required', tags=['specific'])
    def dropdown_should_not_be_required(self, locator):
        element = self.get_element(locator).locator("xpath=./preceding-sibling::*")
        expect(element).not_to_have_class(re.compile(r"required"))

    @keyword('select value')
    def select_value(self, locator, selected_value):
        self.get_element(locator).select_option(label=selected_value, force=True)

    @keyword('select nested value', tags=["specific"])
    def select_nested_value(self, locator, selected_value, wait_for_value=True, unchecked=False):
        element = self.get_element(locator)
        target_label = element.locator(
            f'xpath=/following-sibling::div//label[text()="{selected_value}"]').locator('nth=0')
        element.click()
        if wait_for_value:
            expect(target_label).to_be_visible()
        checkbox = target_label.locator('xpath=/preceding-sibling::input')
        checkbox.check() if not unchecked else checkbox.uncheck()
        element.click(force=True)

    @keyword('nested dropdown should contain', tags=["specific"])
    def nested_dropdown_should_contain(self, locator, *values):
        element = self.get_element(locator)
        element.click(force=True)
        for value in values:
            expect(element.locator(
                f'xpath=/following-sibling::div//label[text()="{value}"]').locator('nth=0')).to_be_visible()
        element.click(force=True)

    @keyword('nested item should be ticked', tags=["specific"])
    def nested_item_should_be_ticked(self, locator, *values):
        element = self.get_element(locator)
        element.click(force=True)
        for value in values:
            expect(element.locator(
                f'xpath=./following-sibling::div//div[@title="{value}"]/input')).to_be_checked()
        element.click(force=True)

    @keyword('nested item should not be ticked', tags=["specific"])
    def nested_item_should_not_be_ticked(self, locator, *values):
        element = self.get_element(locator)
        element.click(force=True)
        for value in values:
            expect(element.locator(
                f'xpath=./following-sibling::div//div[@title="{value}"]/input')).not_to_be_checked()
        element.click(force=True)

    @keyword('nested item should be enabled', tags=["specific"])
    def nested_item_should_be_enabled(self, locator, *values):
        element = self.get_element(locator)
        element.click(force=True)
        for value in values:
            expect(element.locator(
                f'xpath=./following-sibling::div//div[@title="{value}"]/input')).to_be_enabled()
        element.click(force=True)

    @keyword('nested item should be disabled', tags=["specific"])
    def nested_item_should_be_disabled(self, locator, *values):
        element = self.get_element(locator)
        element.click(force=True)
        for value in values:
            expect(element.locator(
                f'xpath=./following-sibling::div//div[@title="{value}"]/input')).to_be_disabled()
        element.click(force=True)

    @keyword('dropdown itemlist should be')
    def dropdown_itemlist_should_be(self, locator, item_list):
        """
        [Documentation]    Verify combobox at ${locator} having correct item list as ${item_list}
        ${item_list} needs to be separated with ';' for each value
        E.g: Robot;Agent;Sale;Customer
        :param locator: element's locator
        :param item_list: Robot;Agent;Sale;Customer
        :return: assert the expected result
        """
        assert self.get_list_values(locator) == item_list.split(
            ";"), f'{self.get_list_values(locator)} is not equal to {item_list.split(";")}'

    @keyword('list item should be')
    def list_item_should_be(self, locator, *item_list):
        """
        [Documentation]    Verify combobox at ${locator} having correct item list as ${item_list}
        ${item_list} needs to be separated with ';' for each value
        E.g: Robot;Agent;Sale;Customer
        :param locator: element's locator - string
        :param item_list: list of string
        :return: assert the expected result
        """
        assert self.get_list_values(locator) == list(item_list), f'{self.get_list_values(locator)} is not equal to ' \
                                                                 f'{item_list}'

    @keyword('dropdown itemlist should contain')
    def dropdown_itemlist_should_contain(self, locator, item_list):
        Robot().should_contain(self.get_list_values(locator), item_list.split(";"))

    @keyword('dropdown itemlist should not contain')
    def dropdown_itemlist_should_not_contain(self, locator, item_list):
        Robot().should_not_contain(self.get_list_values(locator), item_list.split(";"))

    @keyword('dropdown current value should be')
    def dropdown_current_value_should_be(self, locator, expected_value):
        element = self.get_element(locator).locator('xpath=./option[@selected="selected"]')
        expect(element).to_have_text(expected_value)

    @keyword('dropdown current value should not be')
    def dropdown_current_value_should_not_be(self, locator, expected_value):
        element = self.get_element(locator).locator('xpath=./option[@selected="selected"]')
        expect(element).not_to_have_value(expected_value)

    @keyword('dropdown current value should contain')
    def dropdown_current_value_should_contain(self, locator, expected_value):
        element = self.get_element(locator).locator('xpath=./option[@selected="selected"]')
        expect(element).to_contain_text(expected_value)

    @keyword('dropdown current value should not contain')
    def dropdown_current_value_should_not_contain(self, locator, expected_value):
        element = self.get_element(locator).locator('xpath=./option[@selected="selected"]')
        expect(element).not_to_contain_text(expected_value)

    @keyword('get current selected value')
    def get_current_selected_value(self, locator):
        element = self.get_element(locator).locator('xpath=./option[@selected="selected"]')
        return element.input_value()

    @keyword('get list values')
    def get_list_values(self, locator):
        return self.get_element(locator).locator("xpath=./option").all_text_contents()

    @keyword('dropdown should be correct')
    def dropdown_should_be_correct(self, locator, item_list=None, state='enabled', default=None, mandatory=None):
        element = self.get_element(locator)
        # Verify state
        if state == 'enabled':
            self.dropdown_should_be_enabled(element)
        elif state == 'disabled':
            self.dropdown_should_be_disabled(element)
        # Verify default value
        if default is not None:
            self.dropdown_current_value_should_be(element, default)
        # Verify item list
        if item_list is not None:
            self.dropdown_itemlist_should_be(element, item_list)
        # Verify mandatory:
        if mandatory == 'unrequired':
            self.dropdown_should_not_be_required(locator)
        elif mandatory == 'required':
            self.dropdown_should_be_required(locator)

    @keyword('nested dropdown should be correct')
    def nested_dropdown_should_be_correct(self, locator, item_list=None, state='enabled', default=None):
        element = self.get_element(locator)
        # Verify state
        if state == 'enabled':
            expect(element).to_be_enabled()
        elif state == 'disabled':
            assert "disabled" in element.get_attribute("class"), f"{locator} is not disabled"
        # Verify default value
        if default is not None:
            placeholder = element.locator('xpath=./div/p')
            assert default in placeholder.text_content(), f"{locator} is having default value: {placeholder.text}"
        # Verify item list
        if item_list is not None:
            self.nested_dropdown_should_contain(locator, *item_list.split(";"))

    @keyword('get selected item index')
    def get_selected_item_index(self, locator):
        item_list = self.get_list_values(locator)
        return item_list.index(self.get_element(locator).locator("xpath=./option").text_content())

    @keyword('get item list length')
    def get_item_list_length(self, locator):
        return len(self.get_list_values(locator))

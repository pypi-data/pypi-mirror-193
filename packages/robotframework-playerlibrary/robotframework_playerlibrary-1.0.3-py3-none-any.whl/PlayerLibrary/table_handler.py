from playwright.sync_api import expect
from robotlibcore import keyword
from .ui_context import UIContext


class TableHandler(UIContext):

    @keyword('Table column should have')
    def table_column_should_have(self, *items, locator='//table'):
        """
        Check for table header contains some labels or not
        :param locator: element locator
        :param items: list of strings
        :return:
        """
        element = self.get_element(locator)
        for item in items:
            expect(element.locator(f'//thead//tr[contains(.,"{item}")]')).to_be_visible()

    @keyword('Table row should have')
    def table_row_should_have(self, *items, locator='//table', row_index=None):
        """
        Check for table row contains some labels or not
        :param row_index: index of row starting from 1
        :param locator: element locator
        :param items: list of strings
        :return:
        """
        element = self.get_element(locator)
        for item in items:
            if row_index is not None:
                expect(element.locator(f'//tbody//tr[{row_index}][contains(.,"{item}")]')).to_be_visible()
            else:
                item_length = len(items)
                xpath_expression = f'{locator}//tbody//tr['
                for index, item in enumerate(items):
                    if index < item_length - 1:
                        xpath_expression += f'contains(.,"{item}") and '
                    else:
                        xpath_expression += f'contains(.,"{item}")'
                xpath_expression += f']'
                expect(self.page.locator(xpath_expression)).to_be_visible()

    @keyword('Table cell value should be')
    def table_cell_value_should_be(self, row_key, column_name, expected_cell_value):
        """
        Check for specific cell in a table that has expected value
        :param row_key: a specific value in a row that can be identified with others
        :param column_name: name of the column that has the expected cell
        :param expected_cell_value: the expected cell's value
        :return:
        """
        column_titles = self.get_elements(f'//th[.//*[text()="{column_name}"]]/preceding-sibling::*')
        pos = len(column_titles) + 1
        expect(self.page.locator(f'//tr[.//*[text()="{row_key}"]][.//td[position()={pos} '
                                 f'and .//*[text()="{expected_cell_value}"]]]')).to_be_visible()

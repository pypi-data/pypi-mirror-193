import base64

from playwright.sync_api import expect
from robotlibcore import keyword
from .utils import Robot
from .ui_context import UIContext
from .base_context import BaseContext
from .custom_locator import *


class PageHandler(UIContext):
    def __init__(self):
        super().__init__()

    @keyword('page title should be')
    def page_title_should_be(self, title):
        expect(self.get_page()).to_have_title(title)

    @keyword('get all data of similar html elements')
    def get_all_data_of_similar_html_elements(self, locator):
        elements = self.get_elements(locator)
        return [element.text_content() for element in elements]

    @keyword('text should be visible')
    def text_should_be_visible(self, *texts, timeout=BaseContext.SMALL_TIMEOUT):
        for text in texts:
            element = self.get_element(f'//body//*[not(self::script)][contains(.,"{text}")]').first
            expect(element).to_be_visible(timeout=timeout)

    @keyword('text should not be visible')
    def text_should_not_be_visible(self, *texts, timeout=BaseContext.SMALL_TIMEOUT):
        for text in texts:
            element = self.get_element(f'//body//*[not(self::script)][contains(text(),"{text}")]')
            expect(element).to_be_hidden(timeout=timeout)

    @keyword('texts should be visible')
    def texts_should_be_visible(self, texts: list, timeout=BaseContext.TIMEOUT, deep_scan=False):
        text_node = "text()" if not deep_scan else "."
        for text in texts:
            element = self.get_element(f'//body//*[not(self::script)][contains({text_node},"{text}")]')
            expect(element).to_be_visible(timeout=timeout)

    @keyword('texts should not be visible')
    def texts_should_not_be_visible(self, texts: list, timeout=BaseContext.TIMEOUT, deep_scan=False):
        text_node = "text()" if not deep_scan else "."
        for text in texts:
            element = self.get_element(f'//body//*[not(self::script)][contains({text_node},"{text}")]')
            expect(element).to_be_hidden(timeout=timeout)

    @keyword('Page should have')
    def page_should_have(self, *items, timeout=BaseContext.TIMEOUT):
        for item in items:
            if item.startswith(BUILT_IN_PREFIX + CUSTOM_PREFIX + STANDARD_PREFIX + XPATH_PREFIX):
                self.page_should_have_element(item, timeout)
            else:
                self.text_should_be_visible(item)

    @keyword('page should not have')
    def page_should_not_have(self, *items, timeout=BaseContext.TIMEOUT):
        for item in items:
            if item.startswith(BUILT_IN_PREFIX + CUSTOM_PREFIX + STANDARD_PREFIX + XPATH_PREFIX):
                self.page_should_not_have_element(item, timeout)
            else:
                self.text_should_not_be_visible(item)

    @keyword('page should be blank')
    def page_should_be_blank(self):
        expect(self.get_page()).to_have_url("about:blank")

    @keyword('page should have element')
    def page_should_have_element(self, locator, timeout=BaseContext.TIMEOUT):
        element = self.get_element(locator)
        expect(element).to_be_visible(timeout=timeout)
        return element

    @keyword('page should not have element')
    def page_should_not_have_element(self, locator, timeout=BaseContext.SMALL_TIMEOUT, recheck_timeout=2):
        element = self.get_element(locator)
        expect(element).to_be_hidden(timeout=timeout)
        Robot().sleep(recheck_timeout)
        expect(element).to_be_hidden(timeout=timeout)

    @keyword('page should be redirected to')
    def page_should_be_redirected_to(self, url):
        expect(self.get_page()).to_have_url(url)

    @keyword('alert should be shown')
    def alert_should_be_shown(self, content, locator):
        """
        Verifies that an alert is present and, by default, accepts it.
         > ACCEPT: Accept the alert i.e. press Ok. Default.
         > DISMISS: Dismiss the alert i.e. press Cancel.
         > LEAVE: Leave the alert open.
        :param locator:
        :param content:
        :return:
        """
        with self.get_page().expect_event("dialog") as new_dialog_info:
            self.get_element(locator).click()
        dialog = new_dialog_info.value
        assert dialog.message == content
        dialog.dismiss()

    @keyword('capture screenshot')
    def capture_screenshot(self):
        image_bytes = self.get_page().screenshot(full_page=True)
        image_source = base64.b64encode(image_bytes).decode('utf-8')
        image = f"""
        <html>
            <head>
                <style>
                img.one {{
                  height: 75%;
                  width: 75%;
                }}
                </style>
            </head>
            <body>
                <img class="one" src="data:image/png;base64, {image_source}">
            </body>
        </html>   
        """
        Robot().log(message=image, html=True)

    @keyword('get page source')
    def get_page_source(self):
        return self.get_page().text_content()

    @keyword('reload whole page')
    def reload_whole_page(self):
        self.get_page().reload()

    @keyword('html title should be')
    def html_title_should_be(self, title):
        expect(self.get_page()).to_have_title(title)

    @keyword('go back to previous page')
    def go_back_to_previous_page(self):
        self.get_page().go_back()

    @keyword("text having correct amount value")
    def text_having_correct_amount_value(self, text, amount):
        """

        :param text: Something like "I have the payout of {abc} will be refunded tomorrow". Should include the
        curly bracket here
        :param amount: The actual amount which will be replaced into {abc}
        :return: Verify if the text having correct expected amount or not
        """
        text = re.sub(r'(?<=\{).*(?=\})', amount, text)
        text = text.replace("{", "").replace("}", "")
        self.page_should_have(text)

    @keyword('upload file')
    def upload_file(self, file_path, locator='//input[@type="file"]'):
        """
        Handle the upload file function. Locator must point to the element having 'type=file' attribute
        :param locator:
        :param file_path:
        :return: None
        """
        self.get_element(locator).set_input_files(file_path)

    @keyword('wait for text', tags=['deprecated'])
    def wait_for_text(self, text):
        self.text_should_be_visible(text)

    @keyword('wait for text to hide', tags=['deprecated'])
    def wait_for_text_to_hide(self, text):
        self.text_should_not_be_visible(text)

    @keyword('scroll to element', tags=["deprecated"])
    def scroll_to_element(self, locator):
        pass

    @keyword('scroll element into view', tags=["deprecated"])
    def scroll_element_into_view(self, locator):
        pass

    @keyword('scroll to element with additional alignment')
    def scroll_to_element_with_additional_alignment(self, locator, alignment='true'):
        """
        [Documentation]    True - the top of the element will be aligned to the top of the visible area of the scrollable ancestor
        ...    False - the bottom of the element will be aligned to the bottom of the visible area of the scrollable ancestor
        ...    If omitted, it will scroll to the top of the element
        :param locator:
        :param alignment:
        :return:
        """
        element = self.get_element(locator)
        element.evaluate(f"scrollIntoView({alignment});")

    @keyword('scroll right')
    def scroll_right(self):
        self.get_page().evaluate("window.scrollTo(document.body.scrollWidth,document.body.scrollHeight);")

    @keyword('scroll down')
    def scroll_down(self):
        self.get_page().evaluate("window.scrollTo(0,document.body.scrollHeight);")

from playwright.sync_api import expect, Locator
from robotlibcore import keyword
from .custom_locator import *
from .base_context import BaseContext
from .utils import Robot, should_be_equal_as_amounts, rgb_to_hex


class UIContext(BaseContext):
    browser = None
    page = None
    iframe = None
    context = None
    tracing = False
    CHROME_OPTIONS = ["--ignore-certificate-errors", "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                                     "AppleWebKit/537.36 "
                                                     "(KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"]

    def __init__(self):
        super().__init__()
        self.browser =  UIContext.browser
        self.context = UIContext.context
        self.page = UIContext.page
        self.iframe = UIContext.iframe

    def get_browser(self):
        if not UIContext.browser:
            if BaseContext.BROWSER == "chrome":
                UIContext.browser = self.get_player().chromium
            elif BaseContext.BROWSER == "firefox":
                UIContext.browser = self.get_player().firefox
            elif BaseContext.BROWSER == "safari":
                UIContext.browser = self.get_player().webkit
        return UIContext.browser

    def get_page(self):
        if not UIContext.page:
            UIContext.page = self.get_context().new_page()
        return UIContext.page

    def get_context(self, headless=False, device=None, tracing=False, state=None):
        if not UIContext.context:
            if not device:
                UIContext.context = self.get_browser().launch(headless=headless,
                                                        args=UIContext.CHROME_OPTIONS).new_context(storage_state=state)
            else:
                device_model = self.player.devices[device]
                UIContext.context = self.get_browser().launch(
                    headless=headless,
                    args=UIContext.CHROME_OPTIONS).new_context(**device_model)
            if tracing:
                UIContext.context.tracing.start(screenshots=True, snapshots=True, sources=True)
                UIContext.tracing = True
        return UIContext.context

    @keyword('start blank browser')
    def start_blank_browser(self,  headless=False):
        self.player = self.get_player()
        self._setup_custom_locators()
        self.browser = self.get_browser()
        self.context = self.get_context(headless=headless)
        self.page = self.get_page()

    @keyword('start browser then open url')
    def start_browser_then_open_url(self, url, headless=False):
        self.player = self.get_player()
        self._setup_custom_locators()
        self.browser = self.get_browser()
        self.context = self.get_context(headless=headless)
        self.page = self.get_page()
        self.page.goto(url, timeout=BaseContext.BIG_TIMEOUT)
        BaseContext.BASE_URL = url

    @keyword('store storage state')
    def store_storage_state(self):
        BaseContext.STORAGE_STATE = self.context.storage_state()

    @keyword('start incognito browser then open url', tags=['deprecated'])
    def start_incognito_browser_then_open_url(self, url):
        self.start_browser_then_open_url(url)

    @keyword('start new browser session')
    def start_new_browser_session(self):
        Robot().run_keyword_if_test_failed("PlayerLibrary.capture screenshot")
        if UIContext.tracing:
            self.context.tracing.stop(path="trace.zip")
        self.page.evaluate("() => window.localStorage.clear()")
        self.page.evaluate("() => window.sessionStorage.clear()")
        self.context.clear_cookies()
        self.page.reload()
        Robot().sleep(2)
        # self.page.close()
        # self.context.close()
        # UIContext.page = None
        # UIContext.context = None
        # self.context = self.get_context(state=BaseContext.STORAGE_STATE)
        # self.page = self.get_page()

    @keyword('refresh browser session', tags=["deprecated"])
    def refresh_browser_session(self):
        self.page.evaluate("() => window.localStorage.clear()")
        self.page.evaluate("() => window.sessionStorage.clear()")
        self.context.clear_cookies()
        self.page.reload()
        Robot().sleep(2)

    @keyword('go to hard url')
    def go_to_hard_url(self, directory_string, default_host):
        """
        [Documentation]   Enter expected hard url by typing it on Browser Address bar.
        ${directory_string} should be something like /dashboard/agent/booking
        :param directory_string:
        :param default_host:
        :return:
        """
        self.page.goto(f'{default_host}{directory_string}')
        print(f"The url is {default_host}{directory_string}")

    @keyword('go to url')
    def go_to_url(self, url, security_mode=True):
        if security_mode:
            url = url.replace("http://", "https://")
        self.page.goto(url)

    @keyword('go to url in email', tags=["specific"])
    def go_to_url_in_email(self, url, timeout=BaseContext.TIMEOUT, mail_service='mandrillapp'):
        Robot().run_keyword_and_ignore_error('PlayerLibrary.go to url', url, False)
        for sec in range(int(timeout/1000)):
            Robot().sleep(2)
            url = self.page.url
            if mail_service not in url:
                break
        self.page.goto(url.replace('http://', 'https://'))

    @keyword('url should be')
    def url_should_be(self, url):
        expect(self.page).to_have_url(url)

    @keyword('get current url')
    def get_current_url(self):
        return self.page.url

    @keyword('quit all browsers')
    def quit_all_browsers(self):
        self.page.close()
        self.context.close()
        self.player.stop()
        UIContext.page = None
        UIContext.browser = None
        UIContext.context = None
        UIContext.iframe = None
        BaseContext.playwright_context_manager = None
        
    @keyword('close current page')
    def close_current_page(self):
        self.page.close()
        UIContext.page = None

    @keyword('open new window')
    def open_new_window(self):
        UIContext.new_page = self.context.new_page()
        self.page = UIContext.new_page

    @keyword('maximize browser window using js', tags=["deprecated"])
    def maximize_browser_window_using_js(self):
        self.page.evaluate("window.moveTo(0, 0)")
        self.page.evaluate("window.resizeTo(screen.width, screen.height)")

    @keyword("get element")
    def get_element(self, locator):
        if isinstance(locator, Locator):
            return locator
        locator, index = standardize_locator(locator)
        print(f"Formatted locator is `{locator}`")
        print(f"Index of locator is `{index}`")
        return self.get_page().locator(locator).locator(f"nth={index - 1}")

    @keyword("get elements")
    def get_elements(self, locator, timeout=BaseContext.SMALL_TIMEOUT, wait_for_element=False):
        if wait_for_element:
            expect(self.get_element(locator)).to_be_visible(timeout=timeout)
        print(f"Element locator is: {locator}")
        element_list = self.get_page().locator(locator).all()
        print(element_list)
        return element_list

    @keyword('click')
    def click(self, locator, force=False):
        self.get_element(locator).click(force=force)

    @keyword('click using js', tags=["deprecated"])
    def click_using_js(self, locator):
        self.get_element(locator).click(force=True)

    @keyword('click and wait')
    def click_and_wait(self, locator, expected_item=None, expected_text=None, timeout=BaseContext.TIMEOUT):
        element = self.get_element(locator)
        element.click()
        if expected_item:
            expect(self.get_element(expected_item)).to_be_visible(timeout=timeout)
        if expected_text:
            expect(self.get_element(f'//body//*[not(self::script)]'
                                    f'[contains(text(),"{expected_text}")]')).to_be_visible(timeout=timeout)

    @keyword('double click')
    def double_click(self, locator):
        self.get_element(locator).click(click_count=2)

    @keyword('click should open a new tab')
    def click_should_open_a_new_tab(self, locator, url=None, content=None):
        element = self.get_element(locator)
        assert "_blank" == element.get_attribute("target")
        with self.context.expect_page() as new_page_info:
            element.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        self.page = self.context.pages[-1]
        UIContext.page = self.context.pages[-1]
        if url is not None:
            expect(self.page).to_have_url(url)
        if content is not None:
            assert content in self.page.content()

    @keyword('switch to current tab')
    def switch_to_current_tab(self):
        self.page = self.context.pages[0]
        UIContext.page = self.context.pages[0]

    @keyword('switch to current window')
    def switch_to_current_window(self):
        self.page = self.context.pages[0]
        UIContext.page = self.context.pages[0]

    @keyword("hover on")
    def hover_on(self, locator):
        self.get_element(locator).hover()

    @keyword('click should open a new window')
    def click_should_open_a_new_window(self, locator, url=None, content=None):
        element = self.get_element(locator)
        with self.context.expect_page() as new_page_info:
            element.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        self.page = self.context.pages[-1]
        UIContext.page = self.context.pages[-1]
        if url is not None:
            expect(self.page).to_have_url(url)
        if content is not None:
            assert content in self.page.content()

    @keyword('click should open a new popup')
    def click_should_open_a_new_popup(self, locator, url=None, content=None):
        element = self.get_element(locator)
        with self.page.expect_popup() as new_popup_info:
            element.click()
        new_page = new_popup_info.value
        new_page.wait_for_load_state()
        print(self.context.pages)
        self.page = self.context.pages[-1]
        UIContext.page = self.context.pages[-1]
        print(self.page)
        print(UIContext.page)
        if url is not None:
            expect(self.page).to_have_url(url)
        if content is not None:
            assert content in self.page.content()

    @keyword('get actual text')
    def get_actual_text(self, locator):
        element = self.get_element(locator)
        tag = self.get_element_tag(element)
        if tag in ('input', 'textarea', 'select'):
            expect(element).to_have_value(re.compile(r".+"), timeout=BaseContext.SMALL_TIMEOUT)
            actual_text = element.input_value()
        else:
            expect(element).not_to_be_empty(timeout=BaseContext.SMALL_TIMEOUT)
            actual_text = element.inner_text()
        return actual_text

    @keyword("get element tag")
    def get_element_tag(self, locator):
        return self.get_element(locator).evaluate("node => node.tagName")

    @keyword('get actual number')
    def get_actual_number(self, locator):
        text = self.get_actual_text(locator).replace(',', '')
        white_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.']
        number = "".join([char for char in list(text) if char in white_list])
        print(number)
        return number

    @keyword('get inner text')
    def get_inner_text(self, locator):
        return self.get_element(locator).inner_text()

    @keyword('element value should not be empty')
    def element_value_should_not_be_empty(self, locator):
        expect(self.get_element(locator)).not_to_be_empty()

    @keyword('append text')
    def append_text(self, locator, text):
        element = self.get_element(locator)
        original_text = self.get_actual_text(element)
        element.fill(f'{original_text}{text}')

    @keyword('actual text should be')
    def actual_text_should_be(self, locator, expected_value, timeout=BaseContext.SMALL_TIMEOUT):
        actual_text = None
        for sec in range(int(timeout/1000)):
            actual_text = self.get_actual_text(locator)
            if str(actual_text) == str(expected_value):
                break
            Robot().sleep(1)
        if str(actual_text) != str(expected_value):
            raise AssertionError(f"Actual text: '{actual_text}' are different with expected text: '{expected_value}'")

    @keyword('actual text should not be')
    def actual_text_should_not_be(self, locator, expected_value, timeout=BaseContext.SMALL_TIMEOUT):
        actual_text = None
        for sec in range(int(timeout/1000)):
            actual_text = self.get_actual_text(locator)
            if str(actual_text) != str(expected_value):
                break
            Robot().sleep(1)
        if str(actual_text) == str(expected_value):
            raise AssertionError(f"Actual text: '{actual_text}' are similar with expected text: '{expected_value}'")

    @keyword('actual text should contain')
    def actual_text_should_contain(self, locator, expected_value, timeout=BaseContext.SMALL_TIMEOUT):
        actual_text = None
        for sec in range(int(timeout/1000)):
            actual_text = self.get_actual_text(locator)
            if str(expected_value) in str(actual_text):
                break
            Robot().sleep(1)
        if str(expected_value) not in str(actual_text):
            raise AssertionError(f"Actual text: '{actual_text}' does not include the text: '{expected_value}'")

    @keyword('actual text should not contain')
    def actual_text_should_not_contain(self, locator, expected_value, timeout=BaseContext.SMALL_TIMEOUT):
        actual_text = None
        for sec in range(int(timeout/1000)):
            actual_text = self.get_actual_text(locator)
            if str(expected_value) not in str(actual_text):
                break
            Robot().sleep(1)
        if str(expected_value) in str(actual_text):
            raise AssertionError(f"Actual text: '{actual_text}' still includes the text: '{expected_value}'")

    @keyword('actual amount should be')
    def actual_amount_should_be(self, locator, expected_amount, deviation=0.01, timeout=BaseContext.SMALL_TIMEOUT):
        actual_text = None
        for sec in range(int(timeout/1000)):
            actual_text = self.get_actual_text(locator)
        difference = round(float(expected_amount) - float(actual_text), 4)
        if abs(difference) <= deviation:
            pass
        else:
            raise AssertionError(
                f"Actual amount: '{actual_text}' is different with expected amount: '{expected_amount}'")

    @keyword('actual amount should not be')
    def actual_amount_should_not_be(self, locator, expected_amount, deviation=0.01, timeout=BaseContext.SMALL_TIMEOUT):
        actual_text = None
        for sec in range(int(timeout/1000)):
            actual_text = self.get_actual_text(locator)
        difference = round(float(expected_amount) - float(actual_text), 4)
        if abs(difference) > deviation:
            pass
        else:
            raise AssertionError(
                f"Actual amount: '{actual_text}' is likely equal to expected amount: '{expected_amount}'")

    @keyword('actual number should be')
    def actual_number_should_be(self, locator, expected_value):
        should_be_equal_as_amounts(expected_value, self.get_actual_number(locator))

    @keyword('actual number should not be')
    def actual_number_should_not_be(self, locator, expected_value):
        should_be_equal_as_amounts(expected_value, self.get_actual_number(locator))

    @keyword("actual price should be")
    def actual_price_should_be(self, locator, currency: str, expected_amount: str, deviation=0.01, suffix=''):
        """

        :param suffix:
        :param deviation:
        :param locator: element's locator
        :param currency: E.g $, must be a symbol
        :param expected_amount: E.g 124.65
        :return: None
        """
        price_value = self.get_actual_text(locator)
        print(price_value)
        Robot().should_be_equal_as_strings(currency, price_value[:len(currency)])
        Robot().should_be_equal_as_strings(suffix, price_value[len(price_value) - len(suffix):])
        should_be_equal_as_amounts(expected_amount, price_value[len(currency):len(price_value) - len(suffix)],
                                   deviation=deviation)

    @keyword("actual price should not be")
    def actual_price_should_not_be(self, locator: str, currency: str, expected_amount: str):
        """

        :param currency: E.g $
        :param locator: element's locator
        :param expected_amount: E.g 124.65
        :return: None
        """
        price_value = self.get_actual_text(locator)
        if currency != price_value[0] or expected_amount != price_value[1:]:
            raise AssertionError("They are equal to each other!")

    @keyword("element should be marked as required", tags=['specific'])
    def element_should_be_marked_as_required(self, locator):
        element = self.get_element(locator)
        signal_1 = element.locator(f'xpath=/../preceding-sibling::*[contains(@class,"require")]')
        signal_2 = element.locator(f'xpath=/preceding-sibling::*[contains(@class,"require")]')
        assert signal_1.is_visible() or signal_2.is_visible() or ("require" in element.get_attribute("class"))

    @keyword("element should not be marked as required", tags=['specific'])
    def element_should_not_be_marked_as_required(self, locator):
        element = self.get_element(locator)
        signal_1 = element.locator(f'xpath=/../preceding-sibling::*[contains(@class,"require")]')
        signal_2 = element.locator(f'xpath=/preceding-sibling::*[contains(@class,"require")]')
        assert signal_1.is_hidden() or signal_2.is_hidden() or ("require" not in element.get_attribute("class"))

    @keyword("element value should be trimmed")
    def element_value_should_be_trimmed(self, locator):
        raw_string = '123'
        element = self.get_element(locator)
        element.fill(f' {raw_string} ')
        self.lose_focus(element)
        Robot().should_be_equal_as_strings(raw_string, self.get_actual_text(element))

    @keyword("element value should not be trimmed")
    def element_value_should_not_be_trimmed(self, locator):
        raw_string = '123'
        element = self.get_element(locator)
        element.fill(f' {raw_string} ')
        self.lose_focus(element)
        Robot().should_not_be_equal_as_strings(raw_string, self.get_actual_text(element))

    @keyword("lose focus")
    def lose_focus(self, locator):
        self.get_element(locator).blur()

    @keyword("remove element attribute")
    def remove_element_attribute(self, locator, attribute):
        self.get_element(locator).evaluate(f"node => node.removeAttribute('{attribute}')")

    @keyword("drag and drop")
    def drag_and_drop(self, locator, target):
        self.get_element(locator).drag_to(self.get_element(target))

    @keyword("get attribute")
    def get_attribute(self, locator, attribute):
        return self.get_element(locator).get_attribute(attribute)

    @keyword("element should not have attribute")
    def element_should_not_have_attribute(self, locator, attribute, value=""):
        element = self.get_element(locator)
        expect(element).not_to_have_attribute(attribute, value)

    @keyword("element attribute value should be")
    def element_attribute_value_should_be(self, locator, attribute, value):
        element = self.get_element(locator)
        expect(element).to_have_attribute(attribute, value)

    @keyword('element attribute value should contain')
    def element_attribute_value_should_contain(self, locator, attribute, expected_value, timeout=BaseContext.TIMEOUT):
        for sec in range(int(timeout/1000)):
            actual_value = self.get_attribute(locator, attribute)
            if str(expected_value) in str(actual_value):
                break
            Robot().sleep(1)
            if str(expected_value) not in str(actual_value):
                raise AssertionError(f"Actual attribute: '{attribute}' does not include value: '{expected_value}'")

    @keyword('element attribute value should not contain')
    def element_attribute_value_should_not_contain(self, locator, attribute, expected_value,
                                                   timeout=BaseContext.SMALL_TIMEOUT):
        actual_value = None
        for sec in range(int(timeout/1000)):
            actual_value = self.get_attribute(locator, attribute)
            if str(expected_value) not in str(actual_value):
                break
            Robot().sleep(1)
        if str(expected_value) in str(actual_value):
            raise AssertionError(f"Actual attribute: '{attribute}' still includes value: '{expected_value}'")

    @keyword("element should be shown")
    def element_should_be_shown(self, locator, timeout=BaseContext.SMALL_TIMEOUT):
        expect(self.get_element(locator)).to_be_visible(timeout=timeout)

    @keyword("element should not be shown")
    def element_should_not_be_shown(self, locator):
        expect(self.get_element(locator)).to_be_hidden()

    @keyword("element is in an input group", tags=["deprecated", "specific"])
    def element_is_in_an_input_group(self, locator):
        element = self.get_element(locator)
        return True if element.locator(f'xpath=./parent::*/preceding-sibling::*').count() else False

    @keyword("press key")
    def press_keys(self, locator, keys):
        self.get_element(locator).press(keys)

    @keyword("get element count")
    def get_element_count(self, locator):
        return self.page.locator(locator).count()

    @keyword("font size should be")
    def font_size_should_be(self, locator, expected_size):
        size = self.get_css_property_value(locator, "font-size")
        if size != expected_size:
            raise AssertionError(
                f"Element {locator} has fontsize {size}, is not having expected fontsize {expected_size}")

    @keyword("get css property value")
    def get_css_property_value(self, locator, css_property):
        return self.get_element(locator).evaluate(
            f"e =>  window.getComputedStyle(e).getPropertyValue('{css_property}');")

    @keyword("element should have")
    def element_should_have(self, locator, text):
        expect(self.get_element(locator).locator(f"text={text}")).to_be_visible()

    @keyword("element should have these texts")
    def element_should_have_these_texts(self, locator, *texts):
        element = self.get_element(locator)
        for text in texts:
            assert (text in element.text_content()) or element.locator(f'xpath=/*[contains(.,"{text}")]').is_visible()

    @keyword("element should not have")
    def element_should_not_have(self, locator, *texts):
        element = self.get_element(locator)
        for text in texts:
            expect(element.locator(f'xpath=.//*[contains(.,"{text}")]')).to_be_hidden()

    @keyword("get element containing money value", tags=["specific"])
    def get_element_containing_money_value(self, xpath_excluded_money_value, money_value):
        """
        :param xpath_excluded_money_value: Xpath that does not include the money value in it
        :param money_value: the expected money value
        :return: Find all the page to check whether having the expected element or not
        Handle the 0.01 rounding issue of the money value if needed
        """
        rounded_value = round(float(money_value), 2)
        return self.get_element(f'xpath={xpath_excluded_money_value}[contains(.,"{rounded_value}") or '
                                f'contains(.,"{rounded_value + 0.01}") or contains(.,"{rounded_value - 0.01}")]')

    @keyword("tooltip should be correct", tags=["specific"])
    def tooltip_should_be_correct(self, locator, content):
        element = self.get_element(locator)
        element.hover()
        expect(element).to_have_attribute("uib-tooltip", content)

    @keyword("search for inner element")
    def search_for_inner_element(self, locator, inner_locator):
        return self.get_element(locator).locator(f"xpath={inner_locator}")

    @keyword("element color should be")
    def element_color_should_be(self, locator, expected_hex_color, css_properties="color"):
        """
        :param locator: element's locator
        :param css_properties: "color" or "background-color"
        :param expected_hex_color: such as #008040
        :return: raise errors when the color properties are not the same
        """
        raw_color = self.get_css_property_value(locator, css_properties)
        print(raw_color)
        color_tuple = eval(raw_color.replace("rgba", "")) if "rgba" in raw_color else eval(raw_color.replace("rgb", ""))
        hex_color = rgb_to_hex((color_tuple[0], color_tuple[1], color_tuple[2]))
        print(hex_color)
        if hex_color != expected_hex_color:
            raise AssertionError(f"Element {locator} having color is {hex_color}, it is not {expected_hex_color}")

    @keyword("get element color")
    def get_element_color(self, locator, css_properties="color"):
        """
        :param locator: element's locator
        :param css_properties: "color" or "background-color"
        :return: css color of expected element
        """
        raw_color = self.get_css_property_value(locator, css_properties)
        print(raw_color)
        color_tuple = eval(raw_color.replace("rgba", "")) if "rgba" in raw_color else eval(raw_color.replace("rgb", ""))
        hex_color = rgb_to_hex((color_tuple[0], color_tuple[1], color_tuple[2]))
        return hex_color

    @keyword("wait for element", tags=["deprecated"])
    def wait_for_element(self, locator, timeout=BaseContext.SMALL_TIMEOUT):
        expect(self.get_element(locator)).to_be_visible(timeout=timeout)

    @keyword("wait for element to hide", tags=["deprecated"])
    def wait_for_element_to_hide(self, locator, timeout=BaseContext.SMALL_TIMEOUT):
        expect(self.get_element(locator)).to_be_hidden(timeout=timeout)

    @keyword('wait for element to be enabled', tags=["deprecated"])
    def wait_for_element_to_be_enabled(self, locator, timeout=BaseContext.SMALL_TIMEOUT):
        expect(self.get_element(locator)).to_be_enabled(timeout=timeout)

    @keyword('wait for element to be disabled', tags=["deprecated"])
    def wait_for_element_to_be_disabled(self, locator, timeout=BaseContext.SMALL_TIMEOUT):
        expect(self.get_element(locator)).to_be_disabled(timeout=timeout)

    @keyword('should be downloaded normally')
    def should_be_downloaded_normally(self, locator):
        with self.page.expect_download() as download_info:
            self.get_element(locator).click()
        download = download_info.value
        return download.path()

    @keyword('setup custom locator', tags=["deprecated"])
    def setup_custom_locator(self):
        pass

    @keyword('Set Library Search Order', tags=["deprecated"])
    def set_library_search_order(self):
        pass

    @keyword('wait for page to be ready', tags=["deprecated"])
    def wait_for_page_to_be_ready(self):
        pass

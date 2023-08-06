from playwright.sync_api import expect
from robotlibcore import keyword
from .ui_context import UIContext
from .utils import Robot
from .base_context import BaseContext


class PopupHandler(UIContext):

    @keyword('popup should be shown', tags=["specific"])
    def popup_should_be_shown(self, title, timeout=BaseContext.TIMEOUT):
        if '"' in title:
            expect(self.get_element(f"//*[@class='modal-title'][text()='{title}']|"
                                    f"//*[@class='modal-title']/*[text()='{title}']")).to_be_visible(timeout=timeout)
        else:
            expect(self.get_element(f'//*[@class="modal-title"][text()="{title}"]|'
                                    f'//*[@class="modal-title"]/*[text()="{title}"]')).to_be_visible(timeout=timeout)

    @keyword('popup should not be shown', tags=["specific"])
    def popup_should_not_be_shown(self, title, timeout=BaseContext.TIMEOUT):
        if '"' in title:
            expect(self.get_element(f"//*[@class='modal-title'][text()='{title}']|"
                                    f"//*[@class='modal-title']/*[text()='{title}']")).to_be_hidden(timeout=timeout)
        else:
            expect(self.get_element(f'//*[@class="modal-title"][text()="{title}"]|'
                                    f'//*[@class="modal-title"]/*[text()="{title}"]')).to_be_hidden(timeout=timeout)

    @keyword('popup title should have', tags=["specific"])
    def popup_title_should_have(self, title, timeout=BaseContext.TIMEOUT):
        if '"' in title:
            expect(self.get_element(f"//*[@class='modal-title'][contains(.,'{title}')]")).to_be_visible(timeout=timeout)
        else:
            expect(self.get_element(f'//*[@class="modal-title"][contains(.,"{title}")]')).to_be_visible(timeout=timeout)

    @keyword('popup should be closed', tags=["specific"])
    def popup_should_be_closed(self, title=None, timeout=BaseContext.TIMEOUT):
        if not title:
            expect(self.get_element(f'//*[@class="modal-dialog"]')).to_be_hidden(timeout=timeout)
        else:
            if '"' in title:
                expect(self.get_element(f"//*[@class='modal-title'][text()='{title}']")).to_be_hidden(timeout=timeout)
            else:
                expect(self.get_element(f'//*[@class="modal-dialog"]')).to_be_hidden(timeout=timeout)

    @keyword('popup should have', tags=["specific"])
    def popup_should_have(self, *texts, timeout=BaseContext.TIMEOUT):
        for text in texts:
            element = self.get_element('//*[@class="modal-content"]').locator(f"text={text}")
            expect(element).to_be_visible(timeout=timeout)

    @keyword('popup should not have', tags=["specific"])
    def popup_should_not_have(self, expected_text, timeout=BaseContext.SMALL_TIMEOUT):
        element = self.get_element('//*[@class="modal-content"]').locator(f"text={expected_text}")
        expect(element).to_be_hidden(timeout=timeout)

    @keyword('popup should have element', tags=["specific"])
    def popup_should_have_element(self, xpath):
        element = self.get_element('//*[@class="modal-content"]').locator(xpath)
        expect(element).to_be_visible(timeout=BaseContext.SMALL_TIMEOUT)

    @keyword('popup should not have element', tags=["specific"])
    def popup_should_not_have_element(self, xpath):
        element = self.get_element('//*[@class="modal-content"]').locator(xpath)
        expect(element).to_be_hidden(timeout=BaseContext.SMALL_TIMEOUT)

    @keyword('wait for popup to open', tags=["specific"])
    def wait_for_popup_to_open(self, popup_title, timeout=BaseContext.SMALL_TIMEOUT):
        expect(self.get_element(f'//*[@class="modal-title" and text()="{popup_title}"]')).to_be_visible(timeout=timeout)

    @keyword('wait for popup to close', tags=["specific"])
    def wait_for_popup_to_close(self, popup_title, timeout=BaseContext.SMALL_TIMEOUT):
        expect(self.get_element(f'//*[@class="modal-title" and text()="{popup_title}"]')).to_be_hidden(timeout=timeout)

    @keyword('close the popup', tags=["specific"])
    def close_the_popup(self):
        self.get_element('//a[text()="×"]').click()

    @keyword('close any popup', tags=["specific"])
    def close_any_popup(self):
        Robot().sleep(3)
        close_btn = '//a[text()="×"]'
        count = self.get_element(close_btn).count()
        if count > 0:
            self.get_element(close_btn).locator("nth=0").click()

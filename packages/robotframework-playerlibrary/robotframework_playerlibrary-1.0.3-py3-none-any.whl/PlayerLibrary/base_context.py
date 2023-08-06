from playwright.sync_api import sync_playwright
from robotlibcore import keyword
from .custom_locator import *


class BaseContext:
    CHROME_OPTIONS = ["--ignore-certificate-errors", "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                                     "AppleWebKit/537.36 "
                                                     "(KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"]
    TIMEOUT = 45000
    SMALL_TIMEOUT = 15000
    BIG_TIMEOUT = 120000
    BROWSER = "chrome"
    BASE_URL = None
    STORAGE_STATE = None
    playwright_context_manager = None

    def __init__(self):
        self.player = self.get_player()

    def get_player(self):
        if not BaseContext.playwright_context_manager:
            BaseContext.playwright_context_manager = sync_playwright().start()
        return BaseContext.playwright_context_manager
    
    @keyword("set global timeout")
    def set_global_timeout(self, timeout):
        BaseContext.TIMEOUT = timeout

    @keyword("register custom locator")
    def register_custom_locator(self, strategy_name, xpath_mask):
        """
        Register a new locator strategy such as item:Login or btn:Save
        :param strategy_name: The custom strategy name
        :param xpath_mask: The xpath that point to a Locator
        Should contain a placeholder to store the value of the locator strategy
        E.g  xpath_mask = '//a[text()="${label}"]/following-sibling::*[1]'
        The "${label}" placeholder should be declared in the xpath_mask without modifying the name of it
        :return:
        """
        custom_queries = """
              {
                   query(document, label) {
                      let node = document.evaluate(`xpath_mask`, document, null,
                      XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                      return node;
                  },
                   queryAll(document, label) {
                      let xpath = `xpath_mask`;
                      let results = [];
                      let query = document.evaluate(xpath, document,
                          null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
                      for (let i = 0, length = query.snapshotLength; i < length; ++i) {
                          results.push(query.snapshotItem(i));
                      }
                      return results;
                          }
              }
              """
        custom_queries.replace("xpath_mask", xpath_mask)
        self.player.selectors.register(strategy_name, custom_queries)

    def _setup_custom_locators(self):
        self.player.selectors.register('item', QUERY_BY_ITEM)
        self.player.selectors.register('btn', QUERY_BY_BTN)
        self.player.selectors.register('plc', QUERY_BY_PLC)
        self.player.selectors.register('cbx', QUERY_BY_CBX)
        self.player.selectors.register('radio', QUERY_BY_RADIO)
        self.player.selectors.register('link', QUERY_BY_LINK)
        self.player.selectors.register('name', QUERY_BY_NAME)
        self.player.selectors.register('class', QUERY_BY_CLASS)

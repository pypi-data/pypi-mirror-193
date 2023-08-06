import re

BUILT_IN_PREFIX = ('id', 'text', 'data-test-id')
STANDARD_PREFIX = ('plc', 'link', 'name', 'class')
CUSTOM_PREFIX = ('item', 'btn', 'cbx', 'link')
XPATH_PREFIX = ("xpath://", "//")


def standardize_locator(locator: str):
    index = 1
    locator = locator.replace("data-id", "data-test-id")
    if any(prefix for prefix in CUSTOM_PREFIX + BUILT_IN_PREFIX + STANDARD_PREFIX if locator.startswith(prefix)):
        index = get_custom_element_index(locator)
        locator = re.sub(r':', '=', locator, count=1)
        locator = re.sub(r'\[\d+]', '', locator)
        print_xpath(locator)
    else:
        locator = f"{locator}[not(self::script)]"
    return locator, index


def get_custom_element_index(custom_locator):
    """
    Handle the inputted custom locator with or without the index (E.g Customer Name[1])
    Note that index starts from 1 not zero (like xpath expression index)
    :param custom_locator: string with or without the index: E.g "Customer Name[1]"
    :return: a tuple of its index & its actual label
    """
    index = re.search(r'(?<=\[)\d*(?=])', custom_locator)
    if index:
        re.sub(r'\[\d*]$', '', custom_locator)
    return 1 if index is None else int(index.group())


def print_xpath(selector: str):
    prefix, label = selector.split("=")
    if prefix == "item":
        print(f'//label[text()="{label}"]/following-sibling::*[1]')
    elif prefix == "btn":
        print(f'//*[self::button or self::a][contains(.,"{label}") and (contains(@class,"btn") '
              f'or contains(@class,"button"))]')
    elif prefix == "cbx":
        print(f'//label[contains(.,"{label}")]/input[@type="checkbox"]|'
              f'//label[contains(.,"{label}")]/preceding-sibling::*[@type="checkbox"]')
    elif prefix == "radio":
        print(f'//label[text()="{label}"]/preceding-sibling::input')
    elif prefix == "text":
        print(f'//body//*[not(self::script)][contains(text(),"{label}")]')
    elif prefix == "link":
        print(f'//a[contains(.,"{label}")]')
    else:
        print(f'//*[@{prefix}="{label}"]')


QUERY_BY_ITEM = """
      {
           query(document, label) {
              let node = document.evaluate(`//label[text()="${label}"]/following-sibling::*[1]`, document, null,
              XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
              return node;
          },
           queryAll(document, label) {
              let xpath = `//label[text()="${label}"]/following-sibling::*[1]`;
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

QUERY_BY_BTN = """
      {
           query(document, label) {
              return document.evaluate(`//*[self::button or self::a][contains(.,"${label}") and (contains(@class,"btn") 
              or contains(@class,"button"))]`, document, null, 
              XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
          },
           queryAll(document, label) {
              let results = [];
              let query = document.evaluate(`//*[self::button or self::a][contains(.,"${label}") and 
              (contains(@class,"btn") or contains(@class,"button"))]`, document, null, 
              XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
              for (let i = 0, length = query.snapshotLength; i < length; ++i) {
                  results.push(query.snapshotItem(i));
              }
              return results;
                  }
      }
      """

QUERY_BY_PLC = """
      {
           query(document, label) {
              return document.evaluate(`//*[@placeholder="${label}"]`, document, null, 
              XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
          },
           queryAll(document, label) {
              let results = [];
              let query = document.evaluate(`//*[@placeholder="${label}"]`, document, null, 
              XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
              for (let i = 0, length = query.snapshotLength; i < length; ++i) {
                  results.push(query.snapshotItem(i));
              }
              return results;
                  }
      }
      """

QUERY_BY_CBX = """
      {
           query(document, label) {
              return document.evaluate(`//label[contains(.,"${label}")]/input[@type="checkbox"]|
              //label[contains(.,"${label}")]/preceding-sibling::*[@type="checkbox"]`, 
              document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
          },
           queryAll(document, label) {
              let results = [];
              let query = document.evaluate(`//label[contains(.,"${label}")]/input[@type="checkbox"]|
              //label[contains(.,"${label}")]/preceding-sibling::*[@type="checkbox"]`, document, null, 
              XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
              for (let i = 0, length = query.snapshotLength; i < length; ++i) {
                  results.push(query.snapshotItem(i));
              }
              return results;
                  }
      }
      """

QUERY_BY_RADIO = """
      {
           query(document, label) {
              return document.evaluate(`//label[text()="${label}"]/preceding-sibling::input`, document, null, 
              XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
          },
           queryAll(document, label) {
              let results = [];
              let query = document.evaluate(`//label[text()="${label}"]/preceding-sibling::input`, document, null, 
              XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
              for (let i = 0, length = query.snapshotLength; i < length; ++i) {
                  results.push(query.snapshotItem(i));
              }
              return results;
                  }
      }
      """

QUERY_BY_TEXT = """
      {
           query(document, label) {
              return document.evaluate(`//body//*[not(self::script)][contains(text(),"${label}")]`, document, null, 
              XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
          },
           queryAll(document, label) {
              let results = [];
              let query = document.evaluate(`//body//*[not(self::script)][contains(text(),"${label}")]`, document, null, 
              XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
              for (let i = 0, length = query.snapshotLength; i < length; ++i) {
                  results.push(query.snapshotItem(i));
              }
              return results;
                  }
      }
      """

QUERY_BY_LINK = """
      {
           query(document, label) {
              return document.evaluate(`//a[contains(.,"${label}")]`, document, null, 
              XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
          },
           queryAll(document, label) {
              let results = [];
              let query = document.evaluate(`//a[contains(.,"${label}")]`, document, null, 
              XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
              for (let i = 0, length = query.snapshotLength; i < length; ++i) {
                  results.push(query.snapshotItem(i));
              }
              return results;
                  }
      }
      """


QUERY_BY_NAME = """
      {
           query(document, label) {
              return document.evaluate(`//*[@name="${label}"]`, document, null, 
              XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
          },
           queryAll(document, label) {
              let results = [];
              let query = document.evaluate(`//*[@name="${label}"]`, document, null, 
              XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
              for (let i = 0, length = query.snapshotLength; i < length; ++i) {
                  results.push(query.snapshotItem(i));
              }
              return results;
                  }
      }
      """


QUERY_BY_CLASS = """
      {
           query(document, label) {
              return document.evaluate(`//*[@class="${label}"]`, document, null, 
              XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
          },
           queryAll(document, label) {
              let results = [];
              let query = document.evaluate(`//*[@class="${label}"]`, document, null, 
              XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
              for (let i = 0, length = query.snapshotLength; i < length; ++i) {
                  results.push(query.snapshotItem(i));
              }
              return results;
                  }
      }
      """
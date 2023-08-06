# robotframework-playerlibrary
Simple GUI/API automation testing library written in Python using Playwright

Import the library:
```
*** Settings ***
Library           PlayerLibrary
```
Example keyword:
```
*** Keywords ***
Login into the system using provided account
    Input Into    id:login-email       sample-test@abc.com
    Input Into    id:login-password    yourpassword
    Click    //button[contains(.,"Sign In")]
    Page Should Have    Welcome Back!

```
Example scenario:
```
Suite Setup          Start Browser Then Open Url    https://sample-system.com/     headless=True


Test Setup       Login into the system using provided account    AND
Test Teardown       Start new browser session
Suite Teardown      Quit all browsers

*** Test Cases ***
TC_01 - Check correctness of some elements on the screen
    Element Should Be Shown    ${calendar_picker}
    Element Should Be Shown    ${apply_btn}
    Element Should Be Shown    ${clear_btn}
```
Keyword documentation at https://lynhbn.github.io/robotframework-playerlibrary/keyword_document.html

import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cap: Dict[str, Any] = {
    "platformName": "android",
    "automationName": "UIAutomator2",
    "deviceName": "android",
    # "appPackage": "com.socialnmobile.dictapps.notepad.color.note",
    # "appActivity": "com.socialnmobile.colornote.activity.Main",
    "language": "en",
    "locale": "US"

}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

wait = WebDriverWait(driver, timeout= 10)
# Click on APP
el1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@content-desc='COCO']")))
el1.click()

if driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='com.android.permissioncontroller:id/permission_message']").is_displayed():
    driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button").click()
    #Choose Language
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="English").click()
    #Click on Confirm
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Confirm").click()
    #Sign in Info
    uname = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Phone No Or Email"]')
    uname.click()
    uname.send_keys('tuser')
    driver.back()
    password = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Password"]')
    password.click()
    password.send_keys('12345')
    driver.back()
    #Scroll to End
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
    #Click on Sign in
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Sign in").click()


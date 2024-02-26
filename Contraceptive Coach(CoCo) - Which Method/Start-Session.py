import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
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

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Session").click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Skip the tutorial").click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Start session").click()

date = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='YYYY']")
date.click()
date.send_keys('1995')
driver.back()

# driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc='Give the information below What year were you born? Are you currently a student? Yes No What is the highest level of education you have completed?']/android.widget.CheckBox[2]").click()
element = driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.CheckBox')
actions = TouchAction(driver)
actions.press(element[1]).press()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
dropdown = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Choose")
dropdown.click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Completed secondary school").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Start Session").click()



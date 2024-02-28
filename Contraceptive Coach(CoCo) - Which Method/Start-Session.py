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

#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
#Couldn't find correct locator to Select Yes/No
# element = driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.CheckBox')
# actions = TouchAction(driver)
# actions.press(element[1]).perform().release()

dropdown = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Choose")
dropdown.click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Completed secondary school").click()
driver.back()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Start Session").click()

# Test Skip Logic (Pattern 1)
# Q1
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Have you ever had sex?"]/android.widget.ImageView[4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q6
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Now').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q8_1
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q8_2
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

# #Q8_3
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()
# #Q8_4
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()
# #Q8_5
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

# #Q8_6
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

# #Q8_7
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

# #Q8_8
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

# #Q8_9
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

# #Q8_10
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

# #Q8_11
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

# #Q8_12
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

# #Q8_13
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

# #Q8_14
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

# #Q8_15
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

# #Q8_16
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

# #Q8_17
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
# SeekBar Code
seek_bar = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.SeekBar')
start = seek_bar.location['x']
end = seek_bar.size['width']
y = seek_bar.location['y']
action = TouchAction(driver)
# move seekbar to the end
# action.press(x=start, y=y).move_to(x=end, y=y).release().perform()
#move seekbar to 40%
moveTo = (end * 0.45)
action.press(x=start, y=y).move_to(x=moveTo, y=y).release().perform()

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q9
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Have you ever used any '
                                                        'method of contraception?"]/android.widget.ImageView['
                                                        '4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q20_intro
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Next').click()

#Q20
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Do you have at least three periods '
                                             'per year?"]/android.widget.ImageView[3]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q21
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="When you are not using '
                                                        'contraception, do you have very heavy '
                                                        'periods?"]/android.widget.ImageView[4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q22
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="When you are not using '
                                                        'contraception, do you have periods that last longer than 7 '
                                                        'days?"]/android.widget.ImageView[4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()
#Q23
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="When you are not using '
                                             'contraception, do you have painful periods or bad '
                                             'cramps?"]/android.widget.ImageView[4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q24_intro
# driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Next"]').click()
el1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@content-desc='Next']")))
el1.click()

#Q24
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='you are not currently having sex').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q25
Q25 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Type here"]')
Q25.click()
Q25.send_keys('1')
driver.back()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q26_intro
# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Next').click()
el2 = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Next")))
el2.click()

#Q26
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.View/android.widget.ImageView[5]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q27
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.View/android.widget.ImageView[6]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q28
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.View/android.widget.ImageView[4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q29
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Do you have severe acne?"]/android.widget.ImageView[4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q30
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Do you have coarse, dark hairs on '
                                             'your face?"]/android.widget.ImageView[4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q31_intro
# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Next').click()
el3 = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Next")))
el3.click()

#Q31
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="The contraceptive pill requires that '
                                             'you take a pill every single day. Could you remember to take a pill '
                                             'every single day?"]/android.widget.ImageView[3]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q32
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="The contraceptive shot requires that '
                                             'you return to the clinic every three months to get a shot, would you be '
                                             'able to do this?"]/android.widget.ImageView[4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q36
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Would you feel comfortable having an '
                                             'IUD, a T-shaped contraceptive, placed by your provider inside your '
                                             'uterus that would provide contraception for up to 5-10 '
                                             'years?"]/android.widget.ImageView[4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q37
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="The contraceptive implant is one or '
                                             'two small rods placed by your provider under the skin of your upper arm '
                                             'that provides contraception for up to 5 years.  Would you feel '
                                             'comfortable using the contraceptive implant as a contraceptive '
                                             'method?"]/android.widget.ImageView[4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q38
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Other").click()
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q39_intro
# driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Next').click()
el3 = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Next")))
el3.click()

#Q39
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="No").click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q41
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ScrollView/android.view.View/android.widget.ImageView[5]").click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q42
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Have you had surgery in the past '
                                             'three months?"]/android.widget.ImageView[4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q44
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Has a doctor, nurse, or health '
                                             'professional ever told you that you had '
                                             'diabetes?"]/android.widget.ImageView[4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q46
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.View/android.widget.ImageView[5]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q47
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.view.View/android.widget.ImageView[5]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q48
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Do you have an aura with migraine or '
                                             'severe headache? An aura is seeing spots or wavy lines before or during '
                                             'the migraine headache."]/android.widget.ImageView[4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q49
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="No").click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q50
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ScrollView/android.view.View/android.widget.ImageView[5]").click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q51
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ScrollView/android.view.View/android.widget.ImageView[5]").click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q52
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ScrollView/android.view.View/android.widget.ImageView[5]").click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q55
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ScrollView/android.view.View/android.widget.ImageView[4]").click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q56
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ScrollView/android.view.View/android.widget.ImageView[5]").click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q57
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ScrollView/android.view.View/android.widget.ImageView[5]").click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q58
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Do you take dietary supplements or '
                                             'prescription medications regularly?"]/android.widget.ImageView['
                                             '3]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q104
driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Have you ever become pregnant when '
                                             'you did not want to be?"]/android.widget.ImageView[4]').click()
#Scroll to End
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                      'true)).setAsVerticalList().scrollToEnd(5)')
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next").click()

#Q105
el3 = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Next")))
el3.click()

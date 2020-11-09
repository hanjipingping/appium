# _*_coding:utf-8_*_
# @time :2020/11/5 1:08 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :appium_touch.py
# @software PyCharm

from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction
import time

desired_cap = {
    "platformName": "Android",
    "platformVersion": "10",
    "automationName": "UiAutomator2",
    "deviceName": "HUAWEIP30",
    "appPackage": "com.lemon.lemonban",
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity"
}
driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities=desired_cap,
                )

time.sleep(3)

t1 = TouchAction(driver)
element = el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.ImageView")
t1.tap(element=element)
t1.perform()


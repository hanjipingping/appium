# _*_coding:utf-8_*_
# @time :2020/11/5 12:47 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :坐标.py
# @software PyCharm
from appium.webdriver import Remote
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
#点击坐标
driver.tap([(850,1850)],200)

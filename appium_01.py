# _*_coding:utf-8_*_
# @time :2020/11/4 4:10 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :appium_01.py
# @software PyCharm

from appium.webdriver import Remote
import time

from appium.webdriver.common.mobileby import MobileBy

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
#隐形等待
# driver.implicitly_wait(30)
#显性等待

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
WebDriverWait(driver,15,0.5).until(
    EC.element_to_be_clickable((MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("我的柠檬")'))
)


#点击我的
driver.find_element_by_android_uiautomator('new UiSelector().text("我的柠檬")').click()

# el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.ImageView")
# el1.click()
# loc1 = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("点击头像登录")')
# driver.find_element(*loc1).click()
# el2 = driver.find_element_by_id("com.lemon.lemonban:id/fragment_my_lemon_avatar_image")
# el2.click()
#点击头像
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.lemon.lemonban:id/fragment_my_lemon_avatar_image")').click()
#输入用户名
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.lemon.lemonban:id/et_mobile")').send_keys('15011466717')
#输入密码
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.lemon.lemonban:id/et_password") ').send_keys('466717')
#点击登录
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.lemon.lemonban:id/btn_login")').click()
# loc2 = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().id("com.lemon.lemonban:id/et_mobile")')
# driver.find_element(*loc2).click()
# el3 = driver.find_element_by_id("com.lemon.lemonban:id/et_mobile")
# el3.click()
# loc3 = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().id("com.lemon.lemonban:id/et_password")')
# driver.find_element(*loc3).click()
# driver.find_element(*loc3).send_keys('123')

# el4 = driver.find_element_by_id("com.lemon.lemonban:id/et_password")
# el4.click()
# el4.send_keys("466717")
# el5 = driver.find_element_by_id("com.lemon.lemonban:id/btn_login")
# el5.click()

from time import sleep

from appium import webdriver
# 定义字典变量
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
# 字典追加启动参数
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "7.1.2"
desired_caps["deviceName"] = "192.168.56.101:5555"
desired_caps["appPackage"] = "com.android.settings"
desired_caps["appActivity"] = ".Settings"
# 设置中文
desired_caps["unicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True
# 获取driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)
"""
    需求：绘制解锁图案 Z
    绘制坐标点：
        1、1048，340  1377,340  1707，340
        2、1377，669
        3、1048，999  1377，999  1707，999
"""

# 1、定位WLAN
WLAN = driver.find_element_by_xpath("//*[@text='WLAN']")
# 2、定位应用
app = driver.find_element_by_xpath("//*[@text='应用']")

driver.drag_and_drop(app,WLAN)

# 3、点击安全
driver.find_element_by_xpath("//*[@text='安全']").click()
# 4、点击屏幕锁定方式
driver.find_element_by_xpath("//*[@text='屏幕锁定方式']").click()
# 5、点击图案
driver.find_element_by_xpath("//*[@text='图案']").click()
# 必须暂停，登录绘制页面加载完成
sleep(2)
# 6、绘制
TouchAction(driver).press(x=1048,y=340).wait(100).move_to(x=1377,y=340).wait(100).move_to(x=1707,y=340).wait(100)\
    .move_to(x=1377,y=669).wait(100).move_to(x=1048,y=999).wait(100).move_to(x=1377,y=999).wait(100).move_to(x=1707,y=999).wait(100)\
    .perform()


sleep(3)
driver.quit()
from time import sleep

from appium import webdriver
# 定义字典变量
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
# 字典追加启动参数
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "7.1.2"
desired_caps["deviceName"] = "192.168.56.101:5555"
desired_caps["appPackage"] = "com.netease.newsreader.activity"
desired_caps["appActivity"] = "com.netease.nr.phone.main.MainActivity"
# 获取toast
desired_caps['automationName'] = 'Uiautomator2'
# 设置中文
desired_caps["unicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True
# 获取driver /
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)
"""
    需求：
       1、获取网易新闻未同意协议进行登录  --> toast消息
"""




sleep(3)
driver.quit()

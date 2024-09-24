from time import sleep

from appium import webdriver
# 定义字典变量
desired_caps = {}
# 字典追加启动参数
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "7.1.1"
desired_caps["deviceName"] = "192.168.56.101:5555"
desired_caps["appPackage"] = "com.android.settings"
desired_caps["appActivity"] = ".Settings"
# 设置中文
desired_caps["unicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True
# 获取driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

"""
    需求：
        1、启动设置后，暂停3秒，打开短信应用
        2、打印当前默认应用包名启动名
"""
sleep(3)
#  启动短信
driver.start_activity("com.android.messaging",".ui.conversationlist.ConversationListActivity")
# 打印包名和启动名
print("当前所在应用包名：",driver.current_package)
print("当前所在应用启动名：",driver.current_activity)
driver.quit()
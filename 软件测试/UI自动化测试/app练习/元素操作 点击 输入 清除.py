from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import By
# 定义字典变量
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
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

driver.find_element(By.ID,"com.android.settings:id/search").click()
driver.find_element(By.CLASS_NAME,"android.widget.EditText").send_keys("hello")
sleep(2)
driver.find_element(By.CLASS_NAME,"android.widget.EditText").clear()
sleep(2)
driver.find_element(By.CLASS_NAME,"android.widget.EditText").send_keys("你哈")
sleep(2)
driver.quit()
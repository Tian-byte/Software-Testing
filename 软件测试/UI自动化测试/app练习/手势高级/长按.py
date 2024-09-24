from ftplib import ftpcp
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.touch_action import TouchAction

# 定义字典变量
desired_caps = {}
# 字典追加启动参数
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "7.1.2"
desired_caps["deviceName"] = "192.168.56.101:5037"
desired_caps["appPackage"] = "com.android.settings"
desired_caps["appActivity"] = ".Settings"
# 设置中文
desired_caps["unicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True
# 获取driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

# long_press
waln =    driver.find_element(By.CLASS_NAME,"android.widget.LinearLayout")
waln.click()
sleep(3)
waln1 = driver.find_element(By.XPATH,"//*[@text = 'linksys']")
TouchAction(driver).long_press(waln1,duration=3000).perform()

sleep(3)
driver.quit()
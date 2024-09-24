import time

from appium import webdriver

des_cap = dict()
des_cap["platformName"] = "Android"
des_cap["platformVersion"] = "7.1.2"
des_cap["deviceName"] = "emulator-5554"  # 如果只有一个  **** 代替
des_cap["appPackage"] = "com.android.settings"
des_cap["appActivity"] = ".Settings"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_cap)

time.sleep(6)
driver.quit()
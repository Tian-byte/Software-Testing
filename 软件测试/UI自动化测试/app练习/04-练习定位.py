from time import sleep

from appium import webdriver
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


# 使用id 定位放大镜
driver.find_element_by_id("com.android.settings:id/search").click()
sleep(3)
driver.find_element_by_class_name("android.widget.EditText").send_keys("hello")
sleep(3)
driver.find_element_by_xpath("//*[@class='android.widget.ImageButton']").click()
sleep(3)
driver.find_element_by_accessibility_id("搜索设置").click()
sleep(3)
driver.quit()



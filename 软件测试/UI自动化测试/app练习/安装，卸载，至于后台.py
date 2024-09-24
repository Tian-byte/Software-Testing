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
desired_caps["nicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True
# 获取driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)


if driver.is_app_installed("com.yunmall.lc"):
    driver.remove_app("com.yunmall.lc")
    print("卸载成功")
else:
    driver.install_app("E:/Software-Testing/软件测试/UI自动化测试/app练习/bainianaolaitemai_115.apk")
    print('安装成功')

sleep(3)
driver.start_activity("com.android.settings","Settings")
sleep(3)

driver.background_app(3)

driver.close_app()

print("关闭app,后台获取包名为",driver.current_package)
sleep(3)

driver.quit()
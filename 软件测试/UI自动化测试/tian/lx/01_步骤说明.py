from time import sleep

from selenium import webdriver

# 打开谷歌浏览器
driver = webdriver.Chrome()
# 输入url
driver.get("https://hmshop-test.itheima.net/Home/user/login.html")
# 找元素及操作


# 关闭浏览器
sleep(3)
driver.quit()



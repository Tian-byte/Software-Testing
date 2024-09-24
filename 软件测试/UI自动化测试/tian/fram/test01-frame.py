from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("file:///D:/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/09UI/web%E7%AB%AF%E7%8E%AF%E5%A2%83/web%E8%AF%BE%E5%A0%82%E7%B4%A0%E6%9D%90/web/Register.html")
# 页面中iframe 不处理是否能操作
driver.find_element(By.CSS_SELECTOR,"#user").send_keys("admin")
# 注册A操作
# 获取注册A  iframe
A = driver.find_element(By.CSS_SELECTOR,"#idframe1")
# 切换到a
driver.switch_to.frame(A)
driver.find_element(By.CSS_SELECTOR,"#userA").send_keys("admin1")

# 回到默认目录，注册实例。html
driver.switch_to.default_content()

# 获取注册B  iframe
B = driver.find_element(By.CSS_SELECTOR,"#idframe2")
# 切换到a
driver.switch_to.frame(B)
# 注册B
driver.find_element(By.CSS_SELECTOR,"#userB").send_keys("admin2")
sleep(10)
driver.quit()
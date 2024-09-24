from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1获取浏览器驱动
driver = webdriver.Chrome()
#2.打开url
driver.get("file:///D:/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/09UI/web%E7%AB%AF%E7%8E%AF%E5%A2%83/web%E8%AF%BE%E5%A0%82%E7%B4%A0%E6%9D%90/web/%E6%B3%A8%E5%86%8CA.html")

# 3.查找操作元素
# 用户名 admin   id- driver.find_element_by_id("id)
# 元素.send_keys
driver.find_element(By.ID,"userA").send_keys("admin")
# 密码  123456
driver.find_element(By.ID,"passwordA").send_keys("123456")
# 4.关闭浏览器
sleep(3)
driver.quit()
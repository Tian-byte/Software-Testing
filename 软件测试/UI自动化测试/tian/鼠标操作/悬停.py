from time import sleep

from cryptography.hazmat.primitives.asymmetric.ec import derive_private_key
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from win32api import Sleep

driver  = webdriver.Chrome()
driver.get("file:///D:/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/09UI/web%E7%AB%AF%E7%8E%AF%E5%A2%83/web%E8%AF%BE%E5%A0%82%E7%B4%A0%E6%9D%90/web/%E6%B3%A8%E5%86%8CA%E9%BB%84%E8%89%B2.html")
# 获取对象
action = ActionChains(driver)
el = driver.find_element(By.CSS_SELECTOR,"button")
action.move_to_element(el).perform()
sleep(3)
username = driver.find_element(By.CSS_SELECTOR,'#userA')
action.context_click(username).perform()


username.send_keys("admin")
sleep(3)
action.double_click(username).perform()
sleep(3)
driver.quit()
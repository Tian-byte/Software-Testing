from time import sleep

from  selenium import webdriver
from selenium.webdriver.common.by import By

"""
    需求：使用定位一组元素的方法 + teg_name 将注册a页面所有信息进行填写
"""
driver = webdriver.Chrome()

driver.get("file:///D:/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/09UI/web%E7%AB%AF%E7%8E%AF%E5%A2%83/web%E8%AF%BE%E5%A0%82%E7%B4%A0%E6%9D%90/web/%E6%B3%A8%E5%86%8CA.html")

inputs = driver.find_elements(By.TAG_NAME,"input")
# for input in inputs:
#     print(input)



sleep(3)
driver.quit()
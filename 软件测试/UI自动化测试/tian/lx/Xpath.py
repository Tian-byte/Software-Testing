from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///D:/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/09UI/web%E7%AB%AF%E7%8E%AF%E5%A2%83/web%E8%AF%BE%E5%A0%82%E7%B4%A0%E6%9D%90/web/%E6%B3%A8%E5%86%8CA.html")

driver.find_element(By.XPATH,"/html/body/form/div/fieldset/center/p[1]/input").send_keys("admin")
sleep(2)
driver.find_element(By.XPATH,"//p[2]/input").send_keys("123456")
driver.quit()
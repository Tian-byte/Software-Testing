from time import sleep, process_time

from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("file:///D:/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/09UI/web%E7%AB%AF%E7%8E%AF%E5%A2%83/web%E8%AF%BE%E5%A0%82%E7%B4%A0%E6%9D%90/web/%E6%B3%A8%E5%86%8CA%E7%B4%AB%E8%89%B2.html")
print(driver.find_element(By.CSS_SELECTOR, "#userA").size)

print(driver.find_element(By.CSS_SELECTOR, "#fwA").text)
print(driver.find_element(By.CSS_SELECTOR,"#fwA").get_attribute("href"))
print(driver.find_element(By.TAG_NAME,"span").is_displayed())
print(driver.find_element(By.CSS_SELECTOR,"#cancelA").is_enabled())
print(driver.find_element(By.CSS_SELECTOR,"#lia").is_selected())


sleep(3)
driver.quit()
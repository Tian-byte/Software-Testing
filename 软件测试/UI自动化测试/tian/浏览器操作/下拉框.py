from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("file:///D:/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/09UI/web%E7%AB%AF%E7%8E%AF%E5%A2%83/web%E8%AF%BE%E5%A0%82%E7%B4%A0%E6%9D%90/web/%E6%B3%A8%E5%86%8CA%E9%BB%84%E8%89%B2.html")
# driver.find_element(By.CSS_SELECTOR,"[value='gz']").click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR,"[value='sh']").click()
# sleep(2)
# driver.find_element(By.CSS_SELECTOR,"[value='bj']").click()


# 定位下拉框标签
el = driver.find_element(By.CSS_SELECTOR,"#selectA")
# 2.实例化
select = Select(el)
# 使用下表
select.select_by_index(2)
sleep(2)
select.select_by_value("sh")
sleep(2)
select.select_by_visible_text("A北京")
sleep(3)
driver.quit()
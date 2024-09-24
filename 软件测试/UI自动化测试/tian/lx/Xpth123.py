from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://hmshop-test.itheima.net/Home/Index/index.html")

driver.find_element(By.XPATH,"//a[text()='登录']").click()
driver.find_element(By.XPATH,"//input[contains(@placeholder,'手机号/邮箱')]").send_keys("15800000001")
driver.find_element(By.XPATH,"//*[@placeholder='密码']").send_keys("123456")
driver.find_element(By.XPATH,"//input[@class='text_cmu'and @placeholder='验证码' and @name='verify_code']").send_keys("8888")
driver.find_element(By.XPATH,"//*[@class='login_bnt']/a").click()
sleep(3)
driver.quit()
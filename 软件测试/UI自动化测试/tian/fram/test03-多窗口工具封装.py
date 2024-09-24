from time import sleep

from selenium import webdriver

# 1、获取浏览器
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 2、打开url
driver.get("file:///D:/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/%E6%B5%8B%E8%AF%95%E8%B5%84%E6%96%99/09UI/web%E7%AB%AF%E7%8E%AF%E5%A2%83/web%E8%AF%BE%E5%A0%82%E7%B4%A0%E6%9D%90/web/Register.html")


"""
   需求：
        如何随心所欲切换窗口？
    思路：
        1、获取所有窗口句柄
        2、切换窗口
        3、获取当前所在窗口title
        4、判断title是否为需要的窗口
        5、执行代码
    需求：
        1、打开注册示例页面
        2、点击 注册A网页 注册B网页
        3、在A网页和B网页中输入 对用户名输入 admin 
"""


def switch_window(title):
    # 1、获取所有窗口句柄
    handels = driver.window_handles
    # 2、遍历句柄进行切换
    for handel in handels:
        # 操作
        driver.switch_to.window(handel)
        # 获取当前窗口title 并且 判断是否自己需要的窗口
        if driver.title == title:
            # 操作代码
            return "已找到{}窗口，并且已切换成功".format(title)

title_A = "注册A"
title_B = "注册B"

# 打开注册A和注册B网页
driver.find_element(By.LINK_TEXT, "注册A网页").click()
driver.find_element(By.LINK_TEXT, "注册B网页").click()


# 填写注册A网页 用户名
print(switch_window(title_A))
driver.find_element(By.CSS_SELECTOR, "#userA").send_keys("admin")

print(switch_window(title_B))
driver.find_element(By.CSS_SELECTOR, "#userB").send_keys("admin")

# 4、关闭浏览器
sleep(3)
driver.quit()

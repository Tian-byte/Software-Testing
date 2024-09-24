"""
    Base类：存放所有Page页面公共操作方法！
"""
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find(self, loc, timeout=10, poll_frequency=0.5):
        # 显示等待 -> 查找元素  loc = (By.ID,"userA")  *loc=loc[0],loc[1]
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    # 输入方法
    def base_input(self, loc, value):
        # 1、获取元素
        el = self.base_find(loc)
        # 2、清空操作
        el.clear()
        # 3、输入内容
        el.send_keys(value)

    # 点击方法
    def base_click(self, loc):
        self.base_find(loc).click()

    # 获取文本值方法
    def base_get_text(self, loc):
        return self.base_find(loc).text

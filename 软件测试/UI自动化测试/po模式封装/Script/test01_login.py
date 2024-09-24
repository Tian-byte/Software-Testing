import unittest

from selenium import webdriver
from parameterized import parameterized

from page.page_login import PageLogin
from util import read_json


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://hmshop-test.itheima.net/index.php/Home/user/login.html")
        self.login = PageLogin(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    @parameterized.expand(read_json("login.json","login"))
    def test01_login(self,phone,password,code,expect_text):
        # 调用登录业务
       try:
            self.login.page_login(phone,password,code)
            # 断言
            nickname = self.login.page_get_nickname()
            self.assertEqual(nickname,expect_text)
       except Exception as e:
           print(e)
           raise

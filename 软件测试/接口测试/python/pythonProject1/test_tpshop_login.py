import unittest
import requests


from tpshop_login_api import TestTpshopLoginApi

# 分装一个通用的断言
def common_assert(self,resp,status_code,status,msg):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(status, resp.json().get("status"))
    self.assertIn(msg, resp.json().get("msg"))


class TestTpshopLogin(unittest.TestCase):
    session = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.session()

    def setUp(self) -> None:
        TestTpshopLoginApi.get_verify(self.session)

    # 测试登录成功
    def test01_login_ok(self):
        # 获取验证码
        # 登录
        login_data = {"username":"13012345678","password":"123456","verify_code":"8888"}
        resp = TestTpshopLoginApi.login(self.session,login_data)
        # 断言
        print(resp.json())
        common_assert(self, resp, 200, 1,"登陆成功")


    # 测试 手机号不存在
    def test02_tel_not_exists(self):
        data = {"username":"13012347418","password":"123456","verify_code":"8888"}
        res = TestTpshopLoginApi.login(self.session,data)
        print(res.json())
        common_assert(self, res, 200, -1, "账号不存在")


    # 测试 密码错误
    def test03_pwd_err(self):
        # 获取验证码
        data = {"username":"13012345678","password":"12345678","verify_code":"8888"}
        res = TestTpshopLoginApi.login(self.session,data)
        print(res.json())
        common_assert(self, res, 200, -2, "密码错误")

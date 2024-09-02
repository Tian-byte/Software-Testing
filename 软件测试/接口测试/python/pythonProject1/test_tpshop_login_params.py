import unittest
import requests
from parameterized import parameterized

from tpshop_login_api import TestTpshopLoginApi


# 分装一个通用的断言
def common_assert(self, resp, status_code, status, msg):
    self.assertEqual(status_code, resp.status_code)
    self.assertEqual(status, resp.json().get("status"))
    self.assertIn(msg, resp.json().get("msg"))


# 参数化 核心内容
jsondata = [
    {"req_body": {"username": "13012345678", "password": "123456",
                  "verify_code": "8888"},
     "status_code": 200,
     "status": 1,
     "msg": "登陆成功"},
    {"req_body": {"username": "13012345741", "password": "123456",
                  "verify_code": "8888"},
     "status_code": 200,
     "status": -1,
     "msg": "账号不存在"},
    {"req_body": {"username": "13012345678", "password": "123456741",
                  "verify_code": "8888"},
     "status_code": 200,
     "status": -2,
     "msg": "密码错误"}
]


# 格式的转换  将json[{},{},{}] 格式转换为 [(),(),()]元组
# ["a":1,"b":2,"c":3]
# 封装函数 将[(),(),()] 转为 [(),(),()]
def read_json_data():
    list_data = []
    for item in jsondata:
        tmp = tuple(item.values())
        list_data.append(tmp)
# 循环结束 list_data为 [(),(),()]
    return list_data

class TestTpshopLogin(unittest.TestCase):
    session = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.session()

    def setUp(self) -> None:
        TestTpshopLoginApi.get_verify(self.session)

    # 测试登录成功
    @parameterized.expand(read_json_data())
    def test_tpshop_login(self,req_body,status_code,status,msg):
        resp = TestTpshopLoginApi.login(self.session, req_body)
        print(resp.json())
        common_assert(self, resp, status_code, status, msg)

    # # 测试 手机号不存在
    # def test02_tel_not_exists(self):
    #     data = {"username":"13012347418","password":"123456","verify_code":"8888"}
    #     res = TestTpshopLoginApi.login(self.session,data)
    #     print(res.json())
    #     common_assert(self, res, 200, -1, "账号不存在")
    #
    #
    # # 测试 密码错误
    # def test03_pwd_err(self):
    #     # 获取验证码
    #     data = {"username":"13012345678","password":"12345678","verify_code":"8888"}
    #     res = TestTpshopLoginApi.login(self.session,data)
    #     print(res.json())
    #     common_assert(self, res, 200, -2, "密码错误")

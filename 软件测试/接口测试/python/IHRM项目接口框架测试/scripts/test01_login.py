# 完成登录的测试
import json
import unittest
from parameterized import parameterized
from  api.login import LoginAPI

# 构建测试数据
def build_data():
    test_data = []
    # 打开json 文件
    json_file = "../data/login.json"
    with open(json_file,encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            login_data = case_data.get("login_data")





# 创建测试类
class TestLogin(unittest.TestCase):
    # 前置处理
    def setUp(self):
        self.login_api = LoginAPI()
    # 后置处理
    # def tearDown(self):
    #     pass
    @parameterized.expand(build_data)
    def test01_login(self,login_data,status_code,success,code,message):
        resp = self.login_api.login(login_data)
        print(resp.json())

        # 断言
        self.assertEqual(status_code,resp.status_code)
        self.assertEqual(success,resp.json().get("success"))
        self.assertEqual(code,resp.json().get("code"))
        self.assertIn(message,resp.json().get("message"))






    # def test01_case002(self):
    #         # 调用登录接口登录
    #         resp = self.login_api.login({"mobile": "", "password": "888itcast.CN764%..."})
    #         print(resp.json())
    #         # 断言
    #         self.assertEqual(200, resp.status_code)
    #         self.assertEqual(False, resp.json().get("success"))
    #         self.assertEqual(20001, resp.json().get("code"))
    #         self.assertIn("用户名或密码错误", resp.json().get("message"))
    #
    #
    # def test01_case003(self):
    #         # 调用登录接口登录
    #         resp = self.login_api.login({"mobile": "13800000002", "password": " "})
    #         print(resp.json())
    #         # 断言
    #         self.assertEqual(200, resp.status_code)
    #         self.assertEqual(False, resp.json().get("success"))
    #         self.assertEqual(20001, resp.json().get("code"))
    #         self.assertIn("用户名或密码错误", resp.json().get("message"))
    #
    # def test01_case004(self):
    #         # 调用登录接口登录
    #         resp = self.login_api.login(None)
    #         print(resp.json())
    #         # 断言
    #         self.assertEqual(200, resp.status_code)
    #         self.assertEqual(False, resp.json().get("success"))
    #         self.assertEqual(99999, resp.json().get("code"))
    #         self.assertIn("抱歉，系统繁忙，请稍后重试！", resp.json().get("message"))
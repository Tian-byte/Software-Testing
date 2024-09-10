# 导包
import logging
import unittest



import app
from api.user import UserApi


# 定义测试类
class TestUser(unittest.TestCase):
    # 初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        cls.user_api = UserApi()
    # 定义调用接口方法
    # 获取token
    def test01_get_token(self):
        code = app.CODE
        # 准备测试数据
        response = self.user_api.get_token(code)
        json_data =  response.json()
        logging.info(f"获取token的结果为:{json_data}")
        self.assertEqual(200,response.status_code)
        self.assertEqual(32,len(json_data.get("token")))# 断言token值的长度是否为32
        self.assertIn("token",json_data)  # 断言是否包含关键字token
        # 保存token （app.py)
        app.header["token"] = json_data.get("token")
        logging.info(f"保存的token的值：{app.header["token"]}")

    def test02_verify_token(self):
        # 准备测试数据
        token = app.header["token"]
        # 发送请求
        response = self.user_api.verify_token(token)
        json_data = response.json()
        logging.info(f"验证token的结果为：{json_data}")
        # 结果断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(True,json_data.get("isValid"))
        self.assertTrue(json_data.get("isValid"))


    def test03_get_address(self):
        # 准备测试数据

        # 发送请求
        response =  self.user_api.get_address()
        json_data = response.json()
        logging.info(f"获取地址信息为：{json_data}")
        # 断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(app.phone,json_data.get("mobile"))
        self.assertEqual(app.name,json_data.get("name"))
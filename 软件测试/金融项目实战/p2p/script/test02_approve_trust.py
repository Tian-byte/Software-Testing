import unittest
import requests

from parameterized import parameterized
from api import log
from api.api_approve_trust import ApiApproveTrust
from api.api_register_login import ApiRegisterLogin
from util import parser_html, read_json


class TestApproveTrust(unittest.TestCase):
    # 初始化
    # 初始化
    def setUp(self) -> None:
        # 1、获取session
        self.session = requests.session()
        # 2、获取ApiApproveTrust对象
        self.approve = ApiApproveTrust(self.session)
        # 3、调用登录成功
        ApiRegisterLogin(self.session).api_login()

    # 结束
    def tearDown(self) -> None:
        self.session.close()


    # 认证接口测试
    def test01_approve(self):
        # 调用认证接口
        try:
            r = self.approve.api_approve()
            log.info("执行结果为：{}".format(r.text))
            self.assertIn("提交成功",r.text)
            log.info("断言通过：{}")
            print(r.json())
        except Exception as e:
            log.info("断言错误！ 原因：{}".format(e))
            raise


    # 查询认证状态接口测试
    def test02_approve_status(self):
        try:
            r = self.approve.api_approve_status()
            log.info("执行结果为：{}".format(r.text))
            self.assertIn("华", r.text)
            log.info("断言通过")
            print(r.json())
        except Exception as e:
            log.info("断言错误！ 原因：{}".format(e))
            raise

    # 开户接口测试
    def test03_trust(self):
        try:
            r = self.approve.api_trust()
            log.info("执行结果为：{}".format(r.json()))
            self.assertIn("form", r.text)
            print("请求后台开户结果为：",r.json())
            log.info("断言通过")
            # 调用三方开户
            result =  parser_html(r)
            # print(r.json())
            # 期望 (http://xxxx,{"Version":10,})
            # print("result提取结果为：",result)
            r = self.session.post(url=result[0],data=result[1])
            print("三方开户的结果为：",r.text)
            self.assertIn("OK",r.text)
        except Exception as e:
            log.info("断言错误！ 原因：{}".format(e))
            raise

    # 获取图片验证码接口测试
    @parameterized.expand(read_json("approve_trust.json","img_code"))
    def test04_img_code(self,random,expect_text):
        try:
            r = self.approve.api_img_code(random)
            log.info("接口的执行结果为：{}".format(r.status_code))
            self.assertEqual(expect_text,r.status_code)
            log.info("断言通过")
        except Exception as e:
            log.info("断言错误！ 原因：{}".format(e))
            raise

    # 充值接口测试
    @parameterized.expand(read_json("approve_trust.json","recharge"))
    def test05_recharge(self,valicode,expect_text):
        try:
            # 调短信验证码
            self.approve.api_img_code(123)
            r = self.approve.api_recharge(valicode)
            log.info("接口的执行结果为：{}".format(r.json()))
            if valicode == 8888:
                # print("请求后台处理结果为：{}".format(r.json()))
                self.assertIn("form",r.text)
                log.info("断言通过")
                # 三方充值
                result = parser_html(r)
                r = self.session.post(url=result[0], data=result[1])
                print("三方充值的结果为：", r.text)
                self.assertIn(expect_text, r.text)
            else:
                self.assertIn(expect_text,r.text)
        except Exception as e:
            log.info("断言错误！ 原因：{}".format(e))
            raise

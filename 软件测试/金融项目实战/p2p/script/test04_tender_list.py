import unittest

import requests

from api import log
from api.api_approve_trust import ApiApproveTrust
from api.api_register_login import ApiRegisterLogin
from api.api_tender import ApiTender
from util import parser_html


class TestTenderList(unittest.TestCase):
    # 初始化
    def setUp(self) -> None:
        # 获取session
        self.session = requests.session()
        self.reg = ApiRegisterLogin(self.session)
        self.approve = ApiApproveTrust(self.session)
        self.tender = ApiTender(self.session)


    # 结束
    def tearDown(self) -> None:
        self.session.close()

    # 调用接口
    def test01_tender_list(self):
        phone = "1772699567"
        img_code = 8888
        password = "test123"
        phone_code = 666666
        card_id = "690102200509180075"
        # 获取图片验证码
        self.reg.api_img_code(123)
        # 获取短信验证码
        self.reg.api_phone_code(phone,img_code)
        # 注册
        self.reg.api_register(phone,password,img_code,phone_code)
        # 登录
        self.reg.api_login(phone,password)
        # 认证
        self.approve.api_approve(card_id)
        # 后台开户
        r = self.approve.api_trust()
        # 三方开户
        result = parser_html(r)
        r = self.session.post(url=result[0], data=result[1])
        print("三方开户的结果为：", r.text)
        log.info("接口执行结果为：{}".format(r.text))
        # 获取充值验证码
        self.approve.api_img_code(123123)
        # 后台充值
        r = self.approve.api_recharge(img_code)
        # 三方充值
        result = parser_html(r)
        r = self.session.post(url=result[0], data=result[1])
        print("三方充值的结果为：", r.text)
        log.info("接口执行结果为：{}".format(r.text))
        # 后台投资
        r = self.tender.api_tender(100)
        # 三方投资
        result = parser_html(r)
        r = self.session.post(url=result[0], data=result[1])
        print("三方投资的结果为：", r.text)
        log.info("接口执行结果为：{}".format(r.text))
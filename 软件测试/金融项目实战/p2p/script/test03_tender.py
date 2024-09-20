import unittest,requests
from parameterized import parameterized
from api import log
from api.api_register_login import ApiRegisterLogin
from api.api_tender import ApiTender
from util import parser_html, read_json


class TestTender(unittest.TestCase):
    # 初始化
    def setUp(self) -> None:
        # 获取session对象
        self.session = requests.session()
        # 获取 ApiTender对象
        self.tender = ApiTender(self.session)
        # 调用登录
        ApiRegisterLogin(self.session).api_login()

    # 结束
    def tearDown(self) -> None:
        self.session.close()

    # 测试方法
    @parameterized.expand(read_json("tender.json", "tender"))
    def test01_tender(self, amount, expect_text):
        try:
            # 调用投资方法
            r = self.tender.api_tender(amount)
            if amount == 100:
                # 调用三方投资
                result = parser_html(r)
                r = self.session.post(url=result[0], data=result[1])
                print("三方投资的结果为：", r.text)
                log.info("接口执行结果为：{}".format(r.text))
                # 断言
                self.assertIn(expect_text, r.text)
            else:
                self.assertIn(expect_text, r.text)
        except Exception as e:
            log.error(e)
            raise


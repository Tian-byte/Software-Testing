# 测试用例层
import unittest

from assert_util import common_assert
from ihrm_login_api import IhrmLoginApi

class TestIhrmLogin(unittest.TestCase):
    # 测试方法    调用 自己分装的 login接口
    def test01_login_success(self):
        json_data = {"mobile":"13800000002","password":"888itcast.CN764%..."}
        resp = IhrmLoginApi.login(json_data)
        print(resp.json())
        # 断言
        common_assert(self,resp,200,True,10000,"操作成功")


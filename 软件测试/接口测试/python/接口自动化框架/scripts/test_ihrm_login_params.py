# 测试 登录
import unittest

from parameterized import parameterized

from api.ihrm_login_api import IhrmLoginApi
from common.assert_util import assert_util
from common.read_json_util import read_json_data
from config import BASE_DIR

"""
1. 导包 from parameterized import parameterized
2. 在 通用测试方法 上一行添加  @parametterized.expand()
3. 给 expand() 传入元组列表数据 （调用 自己封装的 读取json 文件的函数 read_json_data()）
4. 修改通用测试方法的形参 与json 数据中的 key 一致
5. 在 通用测试方法内 使用形参
"""
class TestIhrmLoginParams(unittest.TestCase):
    path_filename =  BASE_DIR + "/data/ihrm_login.json"
    @parameterized.expand(read_json_data(path_filename))
    def test_login(self,desc,req_data,status_code,success,code,message):
        # 组织请求体数据
        json_data = req_data
        resp = IhrmLoginApi.login(json_data)
        print(desc,":", resp.json())
        # 断言
        assert_util(self, resp, status_code, success, code,message)

import unittest

from parameterized import parameterized

from api.ihrm_emp_curd import IhrmEmpCURD
from common.assert_util import assert_util
from common.db_util import DBUtil
from common.read_json_util import read_json_data
from config import Tel


class TestEmpAddParams(unittest.TestCase):
    # 必选参数
    def setUp(self) -> None:
        delete_sql = f"delete from bs_user where mobile = '{Tel}' "
        DBUtil.uid_db(delete_sql)

    def tearDown(self) -> None:
        delete_sql = f"delete from bs_user where mobile = '{Tel}' "
        DBUtil.uid_db(delete_sql)

    # 添加通用测试方法   实现参数化
    @parameterized.expand(read_json_data())
    def test01_add_emp(self,desc,json_data,status_code,success,code,message):
        # 准备数据
        header = {"content-type":"application/json","authorization":"Bearer b8aa7c83-4fba-490b-b9f4-dca565647968"}
        resp =  IhrmEmpCURD.add_emp(header,json_data)
        # 调用自己分装的接口
        print(resp.json())
        # 添加断言
        assert_util(self,resp,status_code,success,code,message)
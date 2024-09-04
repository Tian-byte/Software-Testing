import unittest

from parameterized import parameterized

from api.ihrm_emp_curd import IhrmEmpCURD
from common.assert_util import assert_util
from common.db_util import DBUtil
from common.get_header import get_header
from common.read_json_util import read_json_data
from config import Tel, BASE_DIR


class TestEmpAddParams(unittest.TestCase):
    header = None
    @classmethod
    def setUpClass(cls) -> None:
        cls.header = get_header()
    # 必选参数
    def setUp(self) -> None:
        delete_sql = f"delete from bs_user where mobile = '{Tel}' "
        DBUtil.uid_db(delete_sql)

    def tearDown(self) -> None:
        delete_sql = f"delete from bs_user where mobile = '{Tel}' "
        DBUtil.uid_db(delete_sql)

    path_filename = BASE_DIR + "/data/ihrm_add.json"
    # 添加通用测试方法   实现参数化
    @parameterized.expand(read_json_data(path_filename))
    def test01_add_emp(self,desc,json_data,status_code,success,code,message):
        # 准备数据
        resp =  IhrmEmpCURD.add_emp(self.header,json_data)
        # 调用自己分装的接口
        print(resp.json())
        # 添加断言
        assert_util(self,resp,status_code,success,code,message)
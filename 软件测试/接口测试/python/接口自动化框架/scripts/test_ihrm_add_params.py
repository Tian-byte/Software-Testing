import unittest


from api.ihrm_emp_curd import IhrmEmpCURD
from common.assert_util import assert_util
from common.db_util import DBUtil
from config import Tel


class TestEmpAdd(unittest.TestCase):
    # 必选参数
    def setUp(self) -> None:
        delete_sql = f"delete from bs_user where mobile = '{Tel}' "
        DBUtil.uid_db(delete_sql)

    def tearDown(self):
        delete_sql = f"delete from bs_user where mobile = '{Tel}' "
        DBUtil.uid_db(delete_sql)

    def test01_add_emp(self):

        # 准备数据
        header = {"content-type":"application/json","authorization":"Bearer b8aa7c83-4fba-490b-b9f4-dca565647968"}
        json_data = {
            "username": "张三",
            "mobile": Tel,
            "workNumber": "9527"
        }

        resp =  IhrmEmpCURD.add_emp(header,json_data)
        # 调用自己分装的接口
        print(resp.json())
        # 添加断言
        assert_util(self,resp,200,True,10000,"操作成功")
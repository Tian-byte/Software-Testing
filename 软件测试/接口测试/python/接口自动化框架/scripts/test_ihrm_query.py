import unittest

from api.ihrm_emp_curd import IhrmEmpCURD
from common.db_util import DBUtil
from common.get_header import get_header


class TestEmpQuery(unittest.TestCase):
    header = None

    @classmethod
    # 测试查询员工
    def setUpClass(cls) -> None:
        cls.header = get_header()

    def setUp(self) -> None:
        insert_sql = "insert into bs_user(id,mobile,username) values('11232456452635',15691075769,'张三')"

        DBUtil.uid_db(insert_sql)

    def tearDown(self) -> None:
        delete_sql = "delete from bs_user where id ='11232456452635';"
        DBUtil.uid_db(delete_sql)
    def test01_query_emp(self):
        resp = IhrmEmpCURD.query_emp("11232456452635", self.header)
        print(resp.json())
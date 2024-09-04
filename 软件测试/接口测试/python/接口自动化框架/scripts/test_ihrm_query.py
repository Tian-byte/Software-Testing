import unittest

from api.ihrm_emp_curd import IhrmEmpCURD
from common.get_header import get_header


class TestEmpQuery(unittest.TestCase):
    header = None

    @classmethod
    # 测试查询员工
    def setUpClass(cls) -> None:
        cls.header = get_header()

    def test01_query_emp(self):
        resp = IhrmEmpCURD.query_emp("1066370498633486336", self.header)
        print(resp.json())
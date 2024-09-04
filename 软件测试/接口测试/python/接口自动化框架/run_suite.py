#  生成测试报告

"""
1.创建测试套件  suit
2.添加测试类
3.创建 HTMLtestReport 类实例  runner
4. runner 调用 run()    suit
"""
import unittest

from htmltestreport import HTMLTestReport


from scripts.test_ihrm_add_params import TestEmpAddParams
from scripts.test_ihrm_login_params import TestIhrmLoginParams

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestIhrmLoginParams))
suite.addTest(unittest.makeSuite(TestEmpAddParams))

runner = HTMLTestReport("./report/ihrm.html")
runner.run(suite)

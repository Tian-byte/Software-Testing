#  生成测试报告

"""
1.创建测试套件  suit
2.添加测试类
3.创建 HTMLtestReport 类实例  runner
4. runner 调用 run()    suit
"""
import logging
import unittest

from htmltestreport import HTMLTestReport


from common.logging_use import init_log_config
from config import BASE_DIR
from scripts.test_ihrm_add_params import TestEmpAddParams
from scripts.test_ihrm_login_params import TestIhrmLoginParams


# 初始化 日志 配置信息
init_log_config(BASE_DIR + "/log/ihrm.log")

suite = unittest.TestSuite()

logging.info("测试套件实例，创建成功!")

suite.addTest(unittest.makeSuite(TestIhrmLoginParams))
suite.addTest(unittest.makeSuite(TestEmpAddParams))

runner = HTMLTestReport("./report/ihrm2.html")
runner.run(suite)
logging.info("ihrm.html 测试报告生成成功")
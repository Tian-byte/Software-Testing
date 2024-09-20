"""
    报告： 使用的插件Htmltestreport
"""
import os

# 1.导包
from htmltestreport import HTMLTestReport
import unittest

from config import DIR_PATH

# 2.组合测试套件
suite = unittest.defaultTestLoader.discover("./script")
# 3.执行测测试套件
report_path = DIR_PATH + os.sep + "report" + os.sep + "p2p.html"
HTMLTestReport(report_path,title="p2p接口自动化测试报告").run(suite)
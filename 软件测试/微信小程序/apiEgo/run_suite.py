# 导包
import time
import  unittest

import app
from script.test_index import TestIndex
from script.test_user import TestUser
from unittestreport import TestRunner

# 创建测试套件对象
suite = unittest.TestSuite()
# 添加测试用例到套件
suite.addTest(unittest.makeSuite(TestIndex))
suite.addTest(unittest.makeSuite(TestUser))
# 批量执行测试用例
# runner = unittest.TextTestRunner() #实例化执行器对象
# runner.run(suite)


# 生成测试报告


# 定义一个测试报告文件
rep_file = app.BASE_DIR + "/report/Ego-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
# 定义第三方执行器对象
runner = TestRunner(suite,  # 测试套件
                    filename=rep_file, #报告文件
                    title="Ego微商项目接口测试报告", # 报告标题
                    tester="tian",# 测试人员
                    desc="V1.0",  # 测试版本
                    templates=1)  # 报告模板
# 直接通过调用run方法执行测试报告
runner.run()
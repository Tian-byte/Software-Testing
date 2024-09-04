# 定义项目的配置信息
# 存放全局变量

import os

# 全局手机号
Tel = "13900043762"


# 全局项目目录
BASE_DIR =  os.path.dirname(__file__)
# 绝对目录 __file__ 将file 放在某个文件 中就可以查处某个问价的路径
print("BASE_DIR",BASE_DIR)
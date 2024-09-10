# 导包
import  logging
from logging import  handlers

import app


# 定义初始化函数
def init_log():
    pass
# 定义日志器
logger = logging.getLogger()  # 初始化日志信息
logger.setLevel(logging.INFO)
# 定义格式化器
sh = logging.StreamHandler()  # 控制台 处理器
log_file = app.BASE_DIR + "/log/Ego.log"
fh = logging.handlers.TimedRotatingFileHandler(log_file,when="D",interval=1,backupCount=7,encoding="UTF-8")
fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"

formatter = logging.Formatter(fmt)
#  设置处理器的格式
sh.setFormatter(formatter)
fh.setFormatter(formatter)
# 将处理器添加到日志器中
logger.addHandler(sh)
logger.addHandler(fh)
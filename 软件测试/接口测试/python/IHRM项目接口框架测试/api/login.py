# 分装api
import requests

# 创建结构类
class LoginAPI(object):
    # 初始化
    def __init__(self):
        # 传入url
        self.url = "https://ihrm-java.itheima.net/api/sys/login"
#  定义接口调用
    def login(self,login_data):
        return  requests.post(url=self.url,json=login_data)
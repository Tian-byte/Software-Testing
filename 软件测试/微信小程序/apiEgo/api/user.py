import requests

import app
from app import header


class UserApi(object):
    # 定义初始化方法（init)
    def __init__(self):
        self.token_url = app.URL + "/api/v1/token/user"
        self.verify_url = app.URL + "/api/v1/token/verify"
        self.address_url = app.URL + "/api/v1/address"
    # 定义接口方法
    def get_token(self,code):
        data = {"code":code}

        return requests.post(self.token_url, headers=app.header, json=data)

    def verify_token(self,token):
        data = {"token":token}
        return requests.post(self.verify_url,headers=app.header,json=data)

    def get_address(self):
        return requests.get(self.address_url,headers=app.header)
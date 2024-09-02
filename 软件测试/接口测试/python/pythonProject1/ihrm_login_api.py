# 接口对象层
import requests

from ihrm登录的普通方法实现 import TestIhrmLogin


class IhrmLoginApi(object):
    @classmethod
    def login(self,json_data):
        resp = requests.post(url="https://ihrm-java.itheima.net/api/sys/login",json=json_data)
        return resp


if __name__ == '__main__':
    data ={"mobile":"13800000002","password":"888itcast.CN764%..."}
    tian =    IhrmLoginApi.login(data)
    print(tian.json())
import unittest

import jsonschema

from api.ihrm_login_api import IhrmLoginApi


class TestIhrmLogin(unittest.TestCase):
    def test01_login(self):
        json_data = {"mobile":"13800000002","password":"888itcast.CN764%..."}
        resp = IhrmLoginApi.login(json_data)
        print("登陆成功",resp.json())

        # 断言校验相应状态码
        self.assertEqual(200,resp.status_code)

        # 校验规则是 返回的resp
        # 校验规则
        schema = {
            "type":"object",
            "properties":{
                "success":{
                    "const":True
                },
                "code":{
                    "const":10000
                },
                "message":{
                    "pattern":"操作成功"
                },
                "data":{
                    "type":"string"
                }
            },
            "required":["success","code","message","data"]
        }

        print(jsonschema.validate(instance=resp.json(), schema=schema))


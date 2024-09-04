from importlib.metadata import requires

import  jsonschema


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
            "const":"操作成功"
        },
        "data":{
            "const":None
        }
    },
    "required":["success","code","message","data"]
}

# 测试数据
data = {
    "success":True,
    "code":10000,
    "message":"操作成功",
    "data": None
}

print(jsonschema.validate(instance=data, schema=schema))
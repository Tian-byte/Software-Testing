import jsonschema

# 准备校验规则
schema = {
    "type":"object",
    "properties":{
        "success":{
            "type":"boolean"
        },
        "code":{
            "type":"integer"
        },
        "message":{
            "type":"string"
        },
        "money":{
            "type":"number"
        },
        "address":{
            "type":"null"
        },
        "data":{"type":"object"},
        "luckyNumber":{
            "type":"array"
        }

    }
}



# 准备校验数据
data = {
    "success" : True,
    "code": 10000,
    "message": "操作成功",
    "money":6.66,
    "address": None,
    "data":{
        "name":"tom"
    },
    "luckyNumber":[6,8,9]
}

print(jsonschema.validate(instance=data, schema=schema))
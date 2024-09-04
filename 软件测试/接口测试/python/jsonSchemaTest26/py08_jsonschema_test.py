import  jsonschema


data = {
    "success":False,
    "code":10000,
    "message":"xxx登陆成功",
    "data":{
        "age":20,
        "name":"lily"
    }
}



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
            "pattern":"登陆成功$"
        },
        "data":{
            "type":"object"
        },
        "properties":{
            "age":{
              "const":20
            },
            "name":{
                "const":"lily"
            }
        }
    },
    "required":["success","code","message","data"]
}

print(jsonschema.validate(instance=data, schema=schema))
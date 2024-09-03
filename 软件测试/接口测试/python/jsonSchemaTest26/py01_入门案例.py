#  导包
import jsonschema

# 创建 校验规则
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
        }
    },
    "required":["success","code","message"]

}


# 准备待测数据校验
data = {
    "success":True,
    "code":10000,
    "message":"操作成功"
}

# 调用 volidate 方法 ，实现校验

print(jsonschema.validate(instance=data, schema=schema))
# 返回 None 校验通过
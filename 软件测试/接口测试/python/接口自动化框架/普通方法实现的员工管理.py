import requests

# 添加员工
url = "https://ihrm-java.itheima.net/api/sys/user"
header = {"content-type":"application/json","authorization":"Bearer b8aa7c83-4fba-490b-b9f4-dca565647968"}

json_data = {
    "username":"张三",
    "mobile":"15691075769",
    "workNumber":"9527"
}

resp = requests.post(url=url,headers=header,json=json_data)

print(resp.json())
# 查询员工
url_query = "https://ihrm-java.itheima.net/api/sys/user/1063705989926227968"
header_query = {"content-type":"application/json","authorization":"Bearer b8aa7c83-4fba-490b-b9f4-dca565647968"}
resp1 = requests.get(url=url_query,headers=header_query)

print(resp1.json())
# 修改员工
url_modify = "https://ihrm-java.itheima.net/api/sys/user/1063705989926227968"
header_modify = {"content-type":"application/json","authorization":"Bearer b8aa7c83-4fba-490b-b9f4-dca565647968"}
modify_data = {"username":"lisi"}
resp2 = requests.put(url = url_modify,headers=header_modify,json=modify_data)
print(resp2.json())
# 删除员工
url_del = "https://ihrm-java.itheima.net/api/sys/user/1063705989926227968"
header_del = {"content-type":"application/json","authorization":"Bearer b8aa7c83-4fba-490b-b9f4-dca565647968"}
resp_del = requests.delete(url = url_del,headers=header_del)
print(resp_del.json())


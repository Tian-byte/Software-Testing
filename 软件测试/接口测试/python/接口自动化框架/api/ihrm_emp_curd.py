# 员工管理模块的接口对象层
import requests


class IhrmEmpCURD(object):
    # 添加员工
    @classmethod
    def add_emp(cls,header,json_data):
        url = "https://ihrm-java.itheima.net/api/sys/user"
        resp = requests.post(url=url, headers=header, json=json_data)
        return resp
    # 查询员工
    @classmethod
    def query_emp(cls,emp_id,header):
        url = "https://ihrm-java.itheima.net/api/sys/user/" + emp_id
        resp = requests.get(url=url, headers=header)
        return resp
    # 修改员工
    @classmethod
    def modify_emp(cls,emp_id,header,modify_data):
        url = "https://ihrm-java.itheima.net/api/sys/user/" + emp_id
        resp = requests.put(url=url, headers=header, json=modify_data)
        return  resp

    # 删除员工
    @classmethod
    def delete_emp(cls,emp_id,header):
        url = "https://ihrm-java.itheima.net/api/sys/user/" + emp_id
        resp = requests.delete(url=url, headers=header)
        return  resp


if __name__ == '__main__':
    header = {"content-type": "application/json", "authorization": "Bearer b8aa7c83-4fba-490b-b9f4-dca565647968"}
    data_add = {
        "username": "张三",
        "mobile": "15691075769",
        "workNumber": "9527"
    }
    a = IhrmEmpCURD.add_emp(header,data_add)
    print(a.json())
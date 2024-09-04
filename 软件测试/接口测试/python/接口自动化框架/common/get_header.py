# 获取登陆成功的令牌 并拼接到请求头  返回
import requests


def get_header():
    url = "https://ihrm-java.itheima.net/api/sys/login"
    data = {"mobile":"13800000002","password":"888itcast.CN764%..."}

    resp = requests.post(url=url,json=data)

    # 从响应体中 获取data 的值
    token = resp.json().get("data")
    header = {"content-type": "application/json",
              "Authorization": "Bearer"+ token}
    return header


if __name__ == '__main__':
    get_header()
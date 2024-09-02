import requests


# 创建session 实例
session = requests.session()
# 使用实例 调用get 发送验证码请求
session.get(url="https://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.4462325060326122")

# 使用实例调用post请求实现登录请求
resp = session.post(url="https://hmshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7231874431560845",
             data={"username":"13012345678","password":"123456","verify_code":"8888"})

print(resp.json())
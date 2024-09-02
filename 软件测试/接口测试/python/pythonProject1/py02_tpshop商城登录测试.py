import unittest

import requests


class TestTpshopLogin(unittest.TestCase):
    # 测试 登录成功
    def test01_login_ok(self):
        session = requests.session()
        session.get(url="https://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.4462325060326122")
        resp = session.post(url="https://hmshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7231874431560845",
             data={"username":"13012345678","password":"123456","verify_code":"8888"})
        print("响应结果 =",resp.json())

        # 添加断言
        self.assertEqual(200,resp.status_code)
        self.assertEqual(1,resp.json().get("status"))
        self.assertEqual("登陆成功",resp.json().get("msg"))
    # 测试 手机号 不存在
    def test02_tel_not_exists(self):
        session = requests.session()
        session.get(url="https://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.4462325060326122")
        resp = session.post(
            url="https://hmshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7231874431560845",
            data={"username": "14744166407", "password": "123456", "verify_code": "8888"})
        print("响应结果 =", resp.json())

        # 添加断言
        self.assertEqual(200, resp.status_code)
        self.assertEqual(-1, resp.json().get("status"))
        self.assertIn("账号不存在", resp.json().get("msg"))
    # 测试密码错误
    def test03_pwd_err(self):
        session = requests.session()
        session.get(url="https://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.4462325060326122")
        resp = session.post(
            url="https://hmshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7231874431560845",
            data={"username": "13012345678", "password": "12345674", "verify_code": "8888"})
        print("响应结果 =", resp.json())

        # 添加断言
        self.assertEqual(200, resp.status_code)
        self.assertEqual(-2, resp.json().get("status"))
        self.assertIn("密码错误", resp.json().get("msg"))
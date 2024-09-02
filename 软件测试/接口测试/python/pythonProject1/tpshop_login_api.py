class  TestTpshopLoginApi(object):
    #  发送验证码请求
    @classmethod
    def get_verify(cls,session):
            session.get(url="https://hmshop-test.itheima.net/index.php?m=Home&c=User&a=verify&r=0.4462325060326122")
    @classmethod
    def login(cls,session,login_data):
        resp = session.post(
            url="https://hmshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7231874431560845",
            data = login_data)
        return resp



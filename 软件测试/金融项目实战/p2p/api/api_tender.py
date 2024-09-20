from config import HOST


class ApiTender:
    # 初始化
    def __init__(self,session):
        # session
        self.session = session
    # 投资方法
        self.__url_tender = HOST + "/trust/trust/tender"
    def api_tender(self,amount):
        # 定义参数
        data = {
            "id":642,
            "depositCertificate":-1,
            "amount":amount
            # "password":""
        }
        return self.session.post(url=self.__url_tender,data=data)
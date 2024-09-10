# 导包

import requests

import app


# 封装测试类
class IndexApi(object):
    # 定义初始化方法(作用：定义实例化之后的对象属性）
    def __init__(self):
        self.banner_url = app.URL + "/api/v1/banner/{}"
        self.theme_url = app.URL + "/api/v1/theme"
        self.recent_product_url = app.URL + "/api/v1/product/recent"
    # 定义接口方法
    # 获取轮播图
    def get_banner(self,banner_id):
        new_url = self.banner_url.format(banner_id)
        return requests.get(new_url)

    def get_theme(self,ids):
        # ?ids=1,2,3  转换为json数据 然后和url 拼接在通过get 方法发送
        # {"ids":"1,2,3"}
        data = {"ids":ids}
        return  requests.get(self.theme_url,params=data)

    def get_recent_product(self):
        return  requests.get(self.recent_product_url)
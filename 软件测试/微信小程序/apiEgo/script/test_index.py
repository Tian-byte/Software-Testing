# 导包
import logging
import  unittest

import app
from api.index import IndexApi


# 定义一个测试类
class TestIndex(unittest.TestCase):
# 初始化方法 已封装类实例化一个对象
    @classmethod
    def setUpClass(cls) ->None:
        cls.index_api = IndexApi()
    #调用获取轮播图接口的方法
    def test01_get_banner(self):
        # 测试数据
        banner_id = app.bid
        # 发送请求
        response =  self.index_api.get_banner(banner_id)
        json_data =  response.json()
        logging.info(f"获取轮播图的结果为:{json_data}")
        # 结果断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(banner_id,json_data.get("id"))
    # 调用获取专题位的接口
    def test02_get_theme(self):
        # 准备测试数据
        ids = app.ids
        # 发送请求
        response = self.index_api.get_theme(ids)
        json_data =  response.json()
        logging.info(f"获取专题栏位的结果为：{json_data}")
        # 结果断言
        self.assertEqual(200,response.status_code)
        # 断言列表的长度大于0 列表不为空
        self.assertIsNotNone(len(json_data))
        # 将列表元素取出来然后在断言
        self.assertEqual(1,json_data[0].get("id"))

    def test03_get_recent(self):
        # 测试数据
        # 发送请求
        response = self.index_api.get_recent_product()
        json_data =  response.json()
        logging.info(f"获取最近新品结果：{json_data}")
        # 结果断言
        self.assertEqual(200,response.status_code)
        self.assertIsNotNone(len(json_data))


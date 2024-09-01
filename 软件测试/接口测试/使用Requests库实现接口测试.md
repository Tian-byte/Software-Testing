# request库

request库：相当于python 当中的浏览器 基于urllib的http库

安装：pip install request    (-i 镜像)

验证：pip show request

``` python
resp = resquest.请求方法(url='URL地址',params={k:v},hearders(k:v),
                    data={k:v},json={k:v},cookies='cookies数据'（如令牌）							) 


# json 和表单 只可以有一种
# resp 响应结果
```

列：访问百度

![image-20240901100824382](E:\Software-Testing\软件测试\接口测试\img\image-20240901100824382.png)













# Cookie及session

简介： 

工程师 针对http协议是无连接，无状态特性，设计的一种技术。可以在浏览器端 存储用户的信息。

特点：

- cookie 用于存储 用户临时的不敏感信息。
- cookie 位于浏览器端, 默认大小 4k(可以调整)
- cookie 中的数据可以随意访问 安全差
- cookie 中存储的数据类型，受浏览器限制

### Cookie + Session 认证发方式 

在计算机中，认证用户身份的方式有多种

-  ihrm项目： token 认证
- tpshop项目： cookie + Session 认证

# Session

session简介

- 也叫会话  通常出现在网络通信中，从客户端借助访问终端登录服务器，直到 退出登录 所产生的 通信数据。保存在会话中

- 特点：·

  - session用于存储 用户临时的不敏感信息。
  - session位于服务端, 数据由服务器规定
  - session中的数据不可以随意访问 安全高
  - session中存储的数据类型，受服务器影响，几乎支持所有的数据 

  Session 自动管理Cookie

  1. Seccion 中的数据 由cookie 传递

  案例：session 实现tpshop 登录

  步骤：

  1. 创建一个Session实例
  1. 使用Sessions实例，调用get方法 发送获取 验证码请求（不获取Cookie)
  1. 使用同一个session实例，调用post方法 发送 登录请求（不携带cookie)
  1. 使用 同一个Session 实例，调用get 方法 发送 查看我的订单请求（不带cookie)
  





### 面试题Cookie 和 Session 区别

1. 数据存储位置： cookies存在在用户端 浏览器    session 存储在服务器端
2. 安全性： cookies的数据可随意访问 不安全   session 安全  加密
3. 数据类型： cookies: 受浏览器限制         session:所有数据类型 直接使用服务器存储
4. 大小： cookies 小   默认4k       session 类型大

```python
import requests
# 1. 创建一个 Session 实例。
session = requests.Session()
# 2. 使用 Session 实例，调 get方法，发送 获取验证码请求。（不需要获取cookie）
resp_v = session.get(url="http://tpshop-test.itheima.net/index.php?
m=Home&c=User&a=verify&r=0.21519623710645064")
# 3. 使用 同一个 Session 实例，调用 post方法，发送 登录请求。(不需要携带 cookie)
resp = session.post(url="http://tpshop-test.itheima.net/index.php?
m=Home&c=User&a=do_login&t=0.7094195931397276",
data={"username": "13012345678", "password": "12345678", "verify_code":
"8888"})
print(resp.json())
# 4. 使用 同一个 Session 实例，调用 get 方法，发送 查看我的订单请求。(不需要携带 cookie)
resp_o = session.get(url="http://tpshop-test.itheima.net/Home/Order/order_list.html")
print(resp_o.text)
```



### 获取指定的相应数据

- 获取URL   resp.url

- 获取相应状态码  resp.status_code

- 获取cookie   resp.cookies

- 获取响应头  resp.hearders

- 获取相应体   

  - 文本格式  resp.text
  - json格式  resp.json()  错

  并不是所有的格式都可以转json





# UnitTest 框架

unitTest 是开发人员用来实现“单元测试” 的框架  测试工程师 可以在自动化“测试执行”的使用

使用UnitTest  的好处

1. 方便管理，维护测试用例
2. 提高丰富的断言方法
3. 生成测试报告



###  UnitTest 框架回顾

TestCase 类

```python
# 1.导包 import unittest
# 2. 定义测试类从 Testcase 类继承

class TestXXX(unittest.TestCase):
  	pass
  
  
# 3.测试方法定义必须以test 开头

class Testxxx(unittest.TestCase):
  	daf test01_xxx(self):
      paa
```

### **fixture **   测试风格

1. 方法级别的  setUp(self) 前  tearDown(self)  后 在每一个普通方法 之前或之后 自动执行
2. 类级别的，  setUpClass(cls)  tearDownClass(cls)  在类内所有方法值 之前/之后 运行一次

```py
# 类： 首字母必须大小，建议以Test开头

import unittest


# 方法： 必须 test 开头  建议 编号
def add(x, y):
    return x + y


class TestADD(unittest.TestCase):
    def setUp(self) -> None:
        print("-------setup-------")

    def tearDown(self) -> None:
            print("------tearDown---")

    @classmethod
    def setUpClass(cls) -> None:
            print("----setupClass--- ")

    @classmethod
    def tearDownClass(cls) -> None:
            print("----tearDownClass----")

    def test01_add(self):
        print("测试方法·1")
        ret = add(10, 20)
        # 断言相应结果
        self.assertEqual(30, ret)

    def test02_add(self):
        print("测试方法2")

        ret = add(100, 200)
    # 断言
        self.assertEqual(300, ret)
```

### **TestSuite ** 测试套件

1. 实例化测试集对象  suite = unittest.TestSuite()
2. 添加指定类的全部测试方法

​		suite.addTest(unittest.makesuite(类名))

​		suite.addTest(unittest.makeSuite(test_dome.TestSum))



​		Testsuite  通过搜索创建测试集 

​		suite = unittest.TestLoader().discover(搜索目录,搜索文件名)

​		suite = unittest.TestLoader().discover ("./","test*py")



### TestRunner

```python
runner = HTMLTestRepot("./report1.html",description="描述信息",title="报告标题")

runner.run(suite)
```





### 完整的测试报告

```py
import unittest

from htmltestreport import HTMLTestReport

from py_unittest_dome import TestADD

#  suite 创建实例
suite = unittest.TestSuite()

# 指定测试类 添加 测试方法
suite.addTest(unittest.makeSuite(TestADD))
# 创建HTMLTestReport 实例
runner =   HTMLTestReport("测试报告.html")
# 调用 run() 传入 suite
runner.run(suite)
```





#### ihrm 登录案例

断言方法:

```python
self.assertEqual(参数1,参数2):
  	参数1: 预期结果. 参数2:实际结果
    成功:完全相等. 断言通过
    失败:报错.
    
    
self.assertIn(参数1,参数2):
  	参数1: 预期结果. 参数2:实际结果
    成功:实际结果中,包含预期结果.断言通过,不报错
    失败:报错
```





### 

```python
import unittest
import requests


class MyTestCase(unittest.TestCase):
    # 登录成功
    def test01_login_ok(self):
        resp =requests.post(url='https://ihrm-java.itheima.net//api/sys/login',
                        json={"mobile": "13800000002","password": "888itcast.CN764%..."})
        # 打印相应结果
        print(resp.json())
        self.assertEqual(200,resp.status_code)
        self.assertEqual(True,resp.json().get("success"))
        self.assertEqual(10000,resp.json().get("code"))
        self.assertIn("操作成功",resp.json().get("message"))
    # 添加测试方法 - 手机号不存在
    def test02_login_ok(self):
        resp = requests.post(url='https://ihrm-java.itheima.net//api/sys/login',
                             json={"mobile": "14744166407","password": "888itcast.CN764%..."})

        print(resp.json())
        self.assertEqual(200,resp.status_code)
        self.assertEqual(False,resp.json().get("success"))
        self.assertEqual(20001,resp.json().get("code"))
        self.assertIn("用户名或密码错误",resp.json().get("message"))


    # 添加测试方法 密码错误
    def test03_login_ok(self):
        resp = requests.post(url='https://ihrm-java.itheima.net//api/sys/login',
                             json={"mobile": "13800000002","password": "123456"})

        print(resp)

        # 断言
        self.assertEqual(200,resp.status_code)
        self.assertEqual(False,resp.json().get("success"))
        self.assertEqual(20001,resp.json().get("code"))
        self.assertIn("用户名或密码错误",resp.json().get("message"))
```

###  报告的生成

```py
import unittest

from htmltestreport import HTMLTestReport

from py11_ihrm_login import MyTestCase

tian = unittest.TestSuite()

tian.addTest(unittest.makeSuite(MyTestCase))

dian = HTMLTestReport("tian.html")

dian.run(tian)
```
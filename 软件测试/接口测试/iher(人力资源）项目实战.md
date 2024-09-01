# IHRM项目实战

### 初始化项目环境

### 新建用例集

<img src="E:\Software-Testing\软件测试\接口测试\img\image-20240831155747097.png" alt="image-20240831155747097" style="zoom:50%;" /> 

### 创建环境

<img src="E:\Software-Testing\软件测试\接口测试\img\image-20240831160348605.png" alt="image-20240831160348605" style="zoom:67%;" /> 

### 



<img src="E:\Software-Testing\软件测试\接口测试\img\image-20240831161127269.png" alt=" "  />

### 添加断言

![image-20240831164632851](E:\Software-Testing\软件测试\接口测试\img\image-20240831164632851.png)

data 的值为令牌不适合断言

### 其他接口共性分析

1. 由于是同一个接口，因此：请求方法 url 请求头 完全一致
2. 测试点（测试用例名） 和 请求数据（请求体），各不相同
3. 响应结果（用作断言） 共三种情况  
   - 操作成功
   - 用户名或密码错误
   - 抱歉系统繁忙

![image-20240831170206749](E:\Software-Testing\软件测试\接口测试\img\image-20240831170206749.png)

### 员工管理业务场景

总析

共两种：

1. 登录成功的令牌，被添加，修改，删除，查询 接口依赖
2. 添加员工成功 得到的 员工id， 被 修改，删除，查询 接口依赖

提取令牌：

代码 写在“登录成功”接口的test 标签页中

```js
// 1.从整个的登录响应结果中获取 json 响应结果

var jsonData = pm.response.json()

// 2.从 json 响应体中 提取data 拼接“Bearer ” 前缀 形成完整的令牌

var token = "Bearer " + jsonData.data
//3.将完整的令牌 保存到环境变量中
pm.environment.set("en_token",token)



// 简化

pm.environment.set("en_token","Bearer " + pm.response.json().data)
```



#### 添加员工

注意：

1. 登录的令牌，在请求头中使用
2. 请求体中的手机号，要保证唯一

提取添加员工的id

```js
// 获取添加员工成功的 响应 json
	var jsonData = pm.response.json()
//提取员工id 

// 设置环境变量
```


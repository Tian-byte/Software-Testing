# postman  高级使用

### postman断言简介

​	postman 断言： 让postman 工具代人工自动判断预期结果和实际结果是否一致

用法：

- ‘Test’



### postman 常用断言

- 断言响应状态

  ``` js
  // 断言响应状态码为200
  pm.test("Status code is 200", function () {
      pm.response.to.have.status(200);
  });
  // 参数1  Status code is 200  在断言结束后显示给用户 断言结果的提示文字
  // 参数2 是一个匿名函数调用 function ()
  //   pm.response.to.have.status(200);  postman中响应状态码 必须有200
  ```

  <img src="E:\软件测试\接口测试\img\image-20240831090232003.png" alt="image-20240831090232003" style="zoom:25%;" /> 说明断言通过

  

- 断言包含某字符串

  ​    Response body: Contains string

```js
pm.test("Body matches string", function () {
    pm.expect(pm.response.text()).to.include("string_you_want_to_search");
});


// expect 希望 期望
// pm.expect(pm.response.text()).to.include("string_you_want_to_search");

//postman 期望 响应文本中 应该包含"你想要搜索的字符串（预期结果） "string_you_want_to_search
```



<img src="E:\软件测试\接口测试\img\image-20240831091207490.png" alt="image-20240831091207490" style="zoom:25%;" />

- 断言Json 数据

​		Response body:JSON value Check

``` js
pm.test("Your test name", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.value).to.eql(100);
});


//  var jsonData = pm.response.json(); 将整个json 响应体 赋值到 jsonData 上
//   pm.expect(jsonData.value).to.eql(100);

//psotman 期望json 结果指定 key的值为xxx
//value 可取值为 success  code message
```

<img src="E:\软件测试\接口测试\img\image-20240831092212709.png" alt="image-20240831092212709" style="zoom:25%;" /> 

### 断言工作原理

<img src="E:\软件测试\接口测试\img\image-20240831092949984.png" alt="image-20240831092949984" style="zoom: 50%;" />



# postman 关联

简介：

当接口和接口之间，有依赖关系时，需要借助postman 关联奇数来实现

如： 登录接口 返回的 令牌 被添加员工接口 依赖

### 实现步骤

<img src="E:\软件测试\接口测试\img\image-20240831093334374.png" alt="image-20240831093334374" style="zoom:50%;" />  

假设： 接口B 产生数据 被接口 A 依赖

1. 发送接口 b 请求 获取响应数据
2. 将响应数据 放入公共容器（全局变量 环境变量）中
3. 接口 A 从 公共容器中 提取数据 发送请求

### 核心代码

```js
// 核心代码：

//1。  获取相应数据 转换为json 格式
var jsonData = pm.response.json();

//2. 设置环境变量  环境变量做容器
pm.environment.set("var_name",value);
// 2.1 使用全局变量
pm.global.set("全局变量名"，全局变量)

//3.引用环境变量
// 请求参数引用： 在postman(url 请求头 hearders  请求体 body)
{{var_name}} 或 {{全局变量名}}
// 代码中引用
var value = pm.enveronment.get("var_name");
```



### 创建环境

-  全局变量：在整个postman 中都可以使用的变量 
- 环境变量 ： 在特殊环境中单独使用



### 案例

<img src="E:\软件测试\接口测试\img\image-20240831094852059.png" alt="image-20240831094852059" style="zoom:50%;" />

1. 使用 postman 关联，实现下面案例 从获取天气接口，http://www.weather.com.cn/data/sk/101010100.html

    获取返回结果中的城市名称 

   调用百度搜索接口： http://www.baidu.com/S?wd=北京 ，把获取到的城市名称，如：北京，作为请求参数

思路：

1. 发送 获取天气请求，获取响应结果 
2. 从响应结果中，拿到城市名，存入 全局变量 
3. 百度搜索接口从 全局变量中，取城市名，发送搜索请求。

<img src="E:\软件测试\接口测试\img\image-20240831100203094.png" alt="image-20240831100203094" style="zoom: 25%;" /> <img src="E:\软件测试\接口测试\img\image-20240831100558551.png" alt="image-20240831100558551" style="zoom:25%;" />

使用 postman 关联技术，实现 添加员工 接口。 

登录成功，返回的 “令牌” 被 添加员工 接口依赖。

 思路：

1. 发送登录请求（必须登录成功），获取响应结果 

2. 从 json 响应结果中，提取 data 值。拼接上 “Bearer ” 前缀。 注意：Bearer单词不能拼错，首字母必须大写，只有一个空格 
3. 将拼接无误的 令牌，存入 环境变量。 从 “眼睛” 图标查看。
4.   添加员工 接口，从 环境变量 中，提取 令牌。设置到请求头中，作为 Authorization 的 值。
5.  填写 添加员工 接口 其他信息（post、URL、请求体），发送请求

<img src="E:\软件测试\接口测试\img\image-20240831112128370.png" alt="image-20240831112128370" style="zoom:50%;" />



# postman 参数化

简介：

测试脚本中仅测试数据不一样，使用参数话提高脚本复用

将测试数据 组织到数据文件 反复迭代 使用不同的数据 达到测试不同用例的目标

**实现步骤**

1. 测试数据保存在 数据文件单独维护
2. 引用数据文件 实现脚本迭代调用

### 数据文件简介

- csv
  - 优点： 数据组织格式简单	
  - 缺点： 
    - 不能测试 bool类型  csv 读取后将非数值类型数据 自动添加 "" 变为字符串
    - 不能存储复杂数据类型  元组 列表 字典
    - 不能实现 参数测试
  - 应用场景： 数据量大 数据组织格式简单
- json
  - 优点
    - 可以测试bool类型
    - 可以使用 复杂数据类型
    - 可以实现 参数测试
  - 缺点
    - 相同数据量，json 文件远大于csv 文件
  - 应用场景 数据量少 数据组织格式复杂  需要进行参数测试

### 编写数据文件

csv 文件

json 文件

### 读取数据文件数据

理论：

根据 使用位置不同，有两种方法

- 请求参数（请求行，请求头，请求体）中，使用 数据文件的数据
- 代码：代码（tests)中，使用 数据文件的数据
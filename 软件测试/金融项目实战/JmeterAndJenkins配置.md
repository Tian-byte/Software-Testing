### 一、Jmeter连接数据库配置

#### 1.1 jmeter连接 数据库

```yacas
jdbc:mysql://52.83.144.39:3306/czbk_member?allowMultiQueries=true

提示：allowMultiQueries=true 允许一次执行多条语句

P2Pmock数据库：
名称：p2p_mock
host：52.83.144.39
port：3306 
username: root 
password: Itcast_p2p_20191228
```

#### 1.2 执行清楚自动化数据 sql语句

```yacas
相关表：
mb_member:用户主表 
mb_member_info:用户信息表 
mb_member_login_log:用户登录日志表 
mb_member_register_log:用户注册日志表
```



```mysql
DELETE i.* from mb_member_info i INNER JOIN mb_member m ON i.member_id = m.id where m.phone in ('${phone1}','${phone2}','${phone3}','${phone4}','${phone5}');

DELETE l.* from mb_member_login_log l INNER JOIN mb_member m ON l.member_id = m.id where  m.phone in ('${phone1}','${phone2}','${phone3}','${phone4}','${phone5}');

DELETE from mb_member_register_log where phone in ('${phone1}','${phone2}','${phone3}','${phone4}','${phone5}');

DELETE from mb_member  where phone in ('${phone1}','${phone2}','${phone3}','${phone4}','${phone5}');
```



### 二、Jenkins配置

#### 2.1 执行命令

```yacas
# 1. windows系统
del result.jtl
rmdir report /S /Q
C:\tools\apache-jmeter-5.0\bin\jmeter.bat -n -t d:/P2P_autotest.jmx -l result.jtl -e -o ./report

# 2. mac
rm -rf result.jtl
rm -rf report
jmeter -n -t /Users/lgy/Documents/传智/课堂工具/jdbc.jmx -l result.jtl -e -o ./report
```

#### 2.2 邮件报告模板

```html
HTML报告模板：
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>${ENV, var="JOB_NAME"}-第${BUILD_NUMBER}次构建日志</title>
</head>
<body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4" offset="0">
<div>
<h2>项目信息</h2>
<ul>
<li>项目名称：${PROJECT_NAME}</li>
<li>详细测试报告：<a href="${PROJECT_URL}HTML_20Report/">${PROJECT_URL}HTML_20Report/</a></li>
<li>触发原因：${CAUSE}</li>
<li>项目Url：<a href="${PROJECT_URL}">${P OJECT_URL}</a></li>
</ul>
<hr/>
<h2>构建日志</h2>
<div>${JELLY_SCRIPT,template="html"}</div>
<hr/>
</div>
</body>
</html>
```

```yacas
# 自定义
<a href="${PROJECT_URL}HTML_20Report/" target="_blank"><h3>测试报告</h3></a>

<a href="${PROJECT_URL}HTML_20Report/" style="color:red;">${PROJECT_URL}HTML_20Report/</a>
```

#### 2.3 解决读取报告无数据问题

> jenkins管理->执行命令

```yacas
System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")
```

```
# -*- coding: utf-8 -*
```


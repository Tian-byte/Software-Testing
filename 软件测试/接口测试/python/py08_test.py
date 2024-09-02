from py07_数据库工具类分装 import DBUtil

var = DBUtil.select_one("select * from goods")
print(var)

DBUtil.uid_db("delete from goods where id = 14")
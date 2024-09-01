
import pymysql



cursor1 = None
conn1= None
try:
    # 建立链接
    conn1 = pymysql.connect(host="localhost",port=3306,user="root",password="tian",
                       database="wms",charset="utf8")
    # 获取游标
    cursor1 = conn1.cursor()
    # 指向0号位置
    # 执行sql语句
    cursor1.execute("select * from goods;")
    # 获取结果
    res1 = cursor1.fetchone()
    cursor1.rownumber = 0
    res2 = cursor1.fetchmany(2)
    cursor1.rownumber = 0
    res3 = cursor1.fetchall()
    cursor1.rownumber = 1
    res4 = cursor1.fetchmany(2)
    print(res4)
    print(res3)
    print(res1)
    print(res2)
except Exception as err:
    print("查询语句出错",str(err))
finally:
    cursor1.close()
    conn1.close()

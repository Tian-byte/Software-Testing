import pymysql

conn = None
cursor = None


try:
    # 连接数据库
    conn = pymysql.connect(host="localhost",port=3306,user="root",password="tian",database="wms",charset="utf8")
    # 设置游标
    cursor = conn.cursor()
    # sql 语句
    cursor.execute("delete from goods where id=1")
    print("影响行数",conn.affected_rows())
    conn.commit()
except Exception as e:
    conn.rollback()
    print("删除失败",str(e))
finally:
    cursor.close()
    conn.close()

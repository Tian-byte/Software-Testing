import pymysql


conn = None
cursor =None

try:
    # 建立连接
    conn = pymysql.connect(host="localhost",port=3306,user="root",password="tian",database="wms",charset="utf8")
    # 游标
    cursor = conn.cursor()
    cursor.execute("update goods set count = 600 where id = 1")
    conn.commit()
except Exception as e:
    print("修改失败",str(e))
    conn.rollback()
finally:
    conn.close()
    cursor.close()
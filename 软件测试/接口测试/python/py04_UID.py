import pymysql



coon7 = None
cursor7 = None


try:
    # 建立连接
    coon7 = pymysql.connect(host="localhost", port=3306, user="root", password="tian",
                        database="wms", charset="utf8")
    # 设置游标
    cursor7 = coon7.cursor()
    # sql
    cursor7.execute("insert into goods(id,name,storage,goodsType,count,remark) values(147,'羽毛球',14,22,40,41);")
    coon7.commit()
except Exception as e:
    print("sql语句错误",str(e))
    coon7.rollback()
finally:
    coon7.close()
    cursor7.close()





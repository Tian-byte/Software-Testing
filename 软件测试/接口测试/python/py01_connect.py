import pymysql

conn = pymysql.connect(host="localhost", port=3306, user="root", password="tian",
                       database="wms", charset="utf8")

cursor = conn.cursor()

cursor.execute("select version()")

res = cursor.fetchone()

print(res[0])

cursor.close()
conn.close()
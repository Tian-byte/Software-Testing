# 分装数据库工具类
import pymysql


class DBUtil(object):
    # 添加类属性
    conn = None
    @classmethod
    def __get_conn(cls):
        # 判断conn 是否为空 如果是在创建
        if cls.conn is None:
            cls.conn = pymysql.connect(host="localhost",port=3306,user="root",password="tian",database="ihrm",charset="utf8")
            #返回非空连接
        return cls.conn

    @classmethod
    def __close_conn(cls):
        if cls.conn is not None:
            cls.conn.close()
            cls.conn = None


    @classmethod
    # 常用方法： 查询 一条
    def select_one(cls,sql):
        cursor = None
        res = None
        try:
            # 获取连接
            cls.coon = cls.__get_conn()
            # 获取游标
            cursor = cls.coon.cursor()
            # 执行sql
            cursor.execute(sql)
            # 提取一条结果
            res = cursor.fetchone()

        except Exception as e:
            print("查询sql错误",str(e))
        finally:
            # 关闭连接
            cursor.close()
            cls.__close_conn()
            return res


    @classmethod
    # 常用方法：增删改
    def uid_db(cls,sql):
        cursor = None
        try:
            # 获取连接
            cls.conn = cls.__get_conn()
            # 获取游标
            cursor = cls.conn.cursor()
            # 执行sql  uid
            cursor.execute(sql)
            print("影响的行数：", cls.conn.affected_rows())
            # 事务
            cls.conn.commit()
        except Exception as e:
            cls.conn.rollback()
            print("增删改sql 执行失败",str(e))
        finally:
            cursor.close()
            cls.__close_conn()



if __name__ == '__main__':
   tian = DBUtil.select_one("select * from goods;")
   print(tian)

   DBUtil.uid_db("delete from goods where id = 2")
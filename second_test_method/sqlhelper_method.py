import pymysql
from second_test_conf.env.config import *


# 数据库连接，执行查询，返回数据
class mysqlHelper(object):
    def __init__(self):
        self.conn = pymysql.connect(**DataBase)
        #返回表的所有数据
    def getDict(self, sql, params):
        # 加**后表示传入的是字典里的数据，否则报错
        #conn = pymysql.connect(**self.conn)
        cur =self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql, params)
        data = cur.fetchall()
        cur.close()
        self.conn.close()
        return data

        #返回表的一行数据
    def getOne(self, sql, params):
    #    conn = pymysql.connect(**self.conn)
        cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql,params)
        data = cur.fetchone()
        cur.close()
        self.conn.close()
        return data
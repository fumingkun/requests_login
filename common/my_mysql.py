# -*- coding: utf-8 -*-
# @Time     : 2021/8/1 16:53
# @Author   : lemon_zhenzhen
# @Email    :544578369@qq.com
# @file     : my_mysql.py
import pymysql
import os
from common.my_conf import MyConf
from common.my_path import conf_dir

class MyMysql:

    def __init__(self):
        #实例化配置对象
        conf = MyConf(os.path.join(conf_dir,"mysql.ini"))
        #1、连接数据库/生成游标
        self.db = pymysql.connect(
            host=conf.get("mysql—游","host"),
            user=conf.get("mysql—游","user"),
            password=conf.get("mysql—游","password"),
            port=conf.getint("mysql—游","port"),
            database=conf.get("mysql—游","database"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        #2、创建游标
        self.cur = self.db.cursor()

    def get_count(self,sql):
        count = self.cur.execute(sql)
        return count

    def get_one_data(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_many_data(self,size=None):
        if size:
            return self.cur.fetchmany(size)
        else:
            return self.cur.fetchall()

    # def update_data(self):
    #     #事务,提交commit，回滚 rollback
    #     pass

    def close_conn(self):
        self.cur.close()
        self.db.close()

if __name__ == "__main__":
    conn = MyMysql()
    sql = "SELECT * FROM `city_user`.`user` where user_id1='301JN2VRGBQP'"
    count = conn.get_count(sql)
    print(count)
    conn.close_conn()












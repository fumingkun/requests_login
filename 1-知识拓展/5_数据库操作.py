# -*- coding: utf-8 -*-
# @Time     : 2021/8/1 11:58
# @Author   : lemon_zhenzhen
# @Email    :544578369@qq.com
# @file     : 5_数据库操作.py
"""
python与各大数据库的连接：
    http://testingpai.com/article/1596527686073
pymysql 安装
pip install pymysql

pymysql 包引入
import pymysql

1、连接数据库
    数据库ip地址
    数据库名
    用户名和密码
    数据库端口：3306
"""
import pymysql
# 1、连接mysql数据库 - 占用数据库资源
db = pymysql.connect(
    host="api.lemonban.com",
    user="future",
    password="123456",
    port=3306,
    database="futureloan",
    charset="utf8"
)
# 2、创建游标
cur = db.cursor()

#3、执行sql语句
sql = "select id from member where mobile_phone='18084856537'"
affected_rows = cur.execute(sql)    #affected_rows 表示执行后的结果 条数

# 4、获取查询结果
# data = cur.fetchone()      # 获取第一个结果
# data = cur.fetchmany(size=2)     # 获取前2行
data = cur.fetchall()      # 获取所有的结果
print(data)

# 5、关闭游标，关闭数据库连接
cur.close()
db.close()





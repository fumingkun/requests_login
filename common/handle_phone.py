# -*- coding: utf-8 -*-
# @Time     : 2021/8/1 18:33
# @Author   : lemon_zhenzhen
# @Email    :544578369@qq.com
# @file     : handle_phone.py
from faker import Faker
from common.my_mysql import MyMysql

def get_new_phone():
    """
    得到没有注册过的手机号码
    1、使用faker生成手机号码
    2、调用mysql数据库操作，去判断是否在数据中存在，如果不在，表示没有注册。
    :return:
    """
    while True:
        phone = Faker("zh_CN").phone_number()
        sql = "SELECT * FROM `city_user`.`user` where user_id='{}'".format(phone)
        res = MyMysql().get_count(sql)
        if res == 0:
            return phone

print(get_new_phone())



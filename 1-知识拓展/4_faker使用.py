# -*- coding: utf-8 -*-
# @Time     : 2021/8/1 11:24
# @Author   : lemon_zhenzhen
# @Email    :544578369@qq.com
# @file     : 4_faker使用.py
from faker import Faker

"""
支持自己定义数据生成规则：
Faker 已经提供了足够丰富的信息生成，包括名字，手机号，邮箱地址，邮编等等，尽管
如此，可能还是没有办法满足你的需求，
这时，可以利用自定义扩展，引用外部的provider，自定义你要的功能。
Faker 对象可以通过 add_provider 方法将自定义的Provider 添加到对象中，
自定义的Provider 需要集成自 BaseProvider.
"""
# 随机生成手机号
f = Faker("zh_CN")
print(f.phone_number())

f = Faker("zh_CN")
print(f.name())



































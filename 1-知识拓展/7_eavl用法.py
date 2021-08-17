# -*- coding: utf-8 -*-
# @Time     : 2021/8/3 22:38
# @Author   : lemon_zhenzhen
# @Email    :544578369@qq.com
# @file     : 7_eavl用法.py
import ast
import json

strr = '{"expected":2500+2000}'

# res = eval(strr)
# print(res)

# ress = ast.literal_eval(strr)
# print(ress)

ress = json.loads(strr)
print(ress)




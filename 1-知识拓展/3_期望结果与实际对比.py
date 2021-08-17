# -*- coding: utf-8 -*-
# @Time     : 2021/7/31 13:00
# @Author   : lemon_zhenzhen
# @Email    :544578369@qq.com
# @file     : 3_期望结果与实际对比.py
import ast
import jsonpath

# 从Excel当中，去取出来的断言列表
# check_str = '[{"expr":"$.msg","expected":"成功","type":"eq"}]'
check_str = '[{"expr":"$.code","expected":0,"type":"eq"}],[{"expr":"$.msg","expected":"成功","type":"eq"}]'
# 把字符串转换成python列表
check_list = ast.literal_eval(check_str)    #比eval安全一点，转成列表
print(check_list)

# 如何从响应结果当中，通过jsonpath表达式，提取出要比对的数据
# 第三方库：jsonpath
response={
    "code": 0,
    "msg": "成功"
}
# 比对结果列表
check_res = []

for check in check_list:
    #通过jsonpath表达式，从响应结果当中拿到实际结果
    actual = jsonpath.jsonpath(response,check["expr"])
    if isinstance(actual,list):
        actual = actual[0]
    #与实际结果做比对
    if check["type"] == "eq":
        check_res.append(actual == check["expected"])

if False in check_res:
    AssertionError









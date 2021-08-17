# -*- coding: utf-8 -*-
# @Time     : 2021/8/1 23:39
# @Author   : lemon_zhenzhen
# @Email    :544578369@qq.com
# @file     : test_2_recharge.py
"""
前置：登录成功
步骤：
断言：

1、类级别的前置  -- 所有充值的用例，只需要登录一次就够了
2、接口关联处理  -- 登录接口的返回值，要提取出来，然后作为充值接口的请求参数

准备知识：re正则表达式  postman是如何处理阐述传递的（接口关联）
"""

import pytest
import json
import os
from common.my_requests import MyRequests
from common.my_excel import MyExcel
from common.my_assert import MyAssert
from common.my_logger import logger
from common.my_path import testdata_dir
from common.handle_phone import get_new_phone

# 第一步，读取注册接口的测试数据 - 是个列表，列表中的每个成员，都是一个接口用例的数据。
# excel_path = r"D:\requests_login\test_excel\cases_1.xlsx"
excel_path = os.path.join(testdata_dir,"cases_1.xlsx")
my = MyExcel(excel_path,"订单列表")
cases = my.read_data()

# 第二步：遍历测试数据，每一组数据，发起一个http的接口
# 实例化请求对象
mq = MyRequests()
massert = MyAssert()

class TestRegister:

    @pytest.mark.parametrize("case", cases)
    def test_regiser(self,case):
        logger.info("===========订单列表===========")
        #1、替换请求数据当中，要替换掉的内容，占位符的形式：#value#
        new_phone = get_new_phone()
        if case["booy"] and case["booy"].find('#phone#') != -1:
            #替换掉占位符 - 请求数据和断言里面替换掉#phone#，替换成未注册手机号码
            logger.info("新生成的手机号码时： \n{}".format(new_phone))
            case["booy"] = case["booy"].replace('#phone#',new_phone)

        # 替换掉占位符 - 请求数据和断言里面替换掉#phone#，替换成未注册手机号码
        if case["assert_list"] and case["assert_list"].find('#phone#') != -1:
            case["assert_list"] = case["assert_list"].replace('#phone#', new_phone)

        # 替换掉占位符 - 请求数据和断言里面替换掉#phone#，替换成未注册手机号码
        if case["assert_db"] and case["assert_db"].find('#user_id#') != -1:
            case["assert_db"] = case["assert_db"].replace('#user_id#', new_phone)

        #2、把替换之后的请求数据（json格式的字符串）。转换成一个字典
        req_dict =json.loads(case["booy"])

        #3、发起请求，并接收响应结果
        resp = mq.send_requests(case["method"],case["url"],req_dict)
        print(resp.json())

        #4、结果空列表
        assert_res = []

        #5、断言响应结果中的数据
        if case["assert_list"]:
            response_check_res = massert.assert_requests_value(case["assert_list"],resp.json())
            assert_res.append(response_check_res)

        #6、断言数据库 - sql语句、结果与实际、比对的类型
        if case["assert_db"]:
            db_check_res = massert.assert_db(case["assert_db"])
            assert_res.append(db_check_res)

        #7、最终的抛AssertionError
        if False in assert_res:
            raise AssertionError


















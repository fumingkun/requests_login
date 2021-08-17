# -*- coding: utf-8 -*-
# @Time     : 2021/8/2 20:28
# @Author   : lemon_zhenzhen
# @Email    :544578369@qq.com
# @file     : test_3_recharge.py
"""
前置：登录成功(意味着要鉴权)
步骤：充值
断言：金额对不对
后置：释放资源/清理数据

1、类级别的前置  -- 所有充值的用例，只需要登录一次就够了，
    登录账号：
        1、用一个固定账号 - 配置化(conf目录下，data.ini里配置用户)
        2、已配置的账号，如何保证它是已经存在的？
            用之前，查一下数据库，如果没有就注册（session前置），

2、接口关联处理  -- 登录接口的返回值，要提取出来，然后作为充值接口的请求参数

准备知识：re正则表达式  postman是如何处理阐述传递的（接口关联）
"""
import pytest
import os
import json
from common.my_conf import MyConf
from common.my_path import conf_dir
from common.my_requests import MyRequests
from common.my_excel import MyExcel
from common.my_assert import MyAssert
from common.my_logger import logger
from common.my_path import testdata_dir

# 第一步，读取注册接口的测试数据 - 是个列表，列表中的每个成员，都是一个接口用例的数据。
# excel_path = r"D:\requests_login\test_excel\cases_1.xlsx"
excel_path = os.path.join(testdata_dir,"cases_1.xlsx")
my = MyExcel(excel_path,"订单列表")
ma = MyExcel(excel_path,"订单详情")
cases = my.read_data()
testcases = ma.read_data()

# 第二步：遍历测试数据，每一组数据，发起一个http的接口
# 实例化请求对象
mq = MyRequests()
massert = MyAssert()



@pytest.fixture(scope="class")
def prepaer():
    #登录
    conf = MyConf(os.path.join(conf_dir,"data.ini"))
    #手机号码
    loginName = conf.get("normal","loginName")
    #验证码
    validateCode = conf.get("normal","validateCode")
    login_url = "member/login/loginBySms"
    data = {"loginName": loginName,"validateCode": validateCode}
    resp = mq.send_requests("post",login_url,data)

    #拿token,id,level_amout
    resp_dict = resp.json()
    # userId = resp_dict["userId"]
    token = resp_dict["token"]
    # mobile = resp_dict["mobile"]
    yield token


@pytest.mark.usefixtures("prepaer")
class TestRecharge:

    @pytest.mark.parametrize("case", cases)
    def test_recharge(self,case,prepaer):
        # 1、接收前置的返回值，-- 上一个接口的返回值，提取出来，
        token = prepaer
        #替换headers中的token
        a = mq.headers['city-token'] = token
        logger.info("从上一个接口提取出来的数据为：\n token:{}".format(token))

        #3、把替换之后的请求数据（json格式的字符串）。转换成一个字典
        req_dict =json.loads(case["booy"])

        #4、发起请求，并接收响应结果
        resp = mq.send_requests(case["method"],case["url"],req_dict)
        logger.info(resp.json())
        resp_dict = resp.json()
        orderNo = json.loads(resp_dict["result"]["orderList"][0]["detail"])["orderNo"]
        subOrderNo = json.loads(resp_dict["result"]["orderList"][0]["detail"])["subOrderNo"]
        yield orderNo, subOrderNo

@pytest.mark.usefixtures("prepaer","TestRecharge")
class TestDetail:

    @pytest.mark.parametrize("testcase", testcases)
    def test_recharge(self,testcase,prepaer,TestRecharge):
        # 1、接收前置的返回值，-- 上一个接口的返回值，提取出来，
        token = prepaer
        #替换headers中的token
        logger.info("从上一个接口提取出来的数据为：\n token:{}".format(token))

        orderNo,subOrderNo = TestRecharge
        logger.info("从上一个接口提取出来的数据为：\n orderNo:{} \n subOrderNo:{}".format(orderNo,subOrderNo))

        #2、下一个接口的请求数据中，需要替换，替换为上一个接口中提取的数据，
        if testcase["booy"] and testcase["booy"].find('#token#') != -1:
            #替换掉占位符 - 请求数据和断言里面替换掉#token#，替换成有效的token
            # logger.info("新生成的手机号码时： \n{}".format(token))
            testcase["booy"] = testcase["booy"].replace('#token#', token)
            testcase["booy"] = testcase["booy"].replace('#orderNo#', orderNo)
            testcase["booy"] = testcase["booy"].replace('#subOrderNo#',subOrderNo)


        #3、把替换之后的请求数据（json格式的字符串）。转换成一个字典
        req_dict =json.loads(testcase["booy"])

        #4、发起请求，并接收响应结果
        resp = mq.send_requests(testcase["method"],testcase["url"],req_dict)
        logger.info(resp.json())

        #5、结果空列表
        assert_res = []

        #6、断言响应结果中的数据
        if testcase["assert_list"]:
            response_check_res = massert.assert_requests_value(testcase["assert_list"],resp.json())
            assert_res.append(response_check_res)

        #7、断言数据库 - sql语句、结果与实际、比对的类型
        if testcase["assert_db"]:
            db_check_res = massert.assert_db(testcase["assert_db"])
            assert_res.append(db_check_res)

        #8、最终的抛AssertionError
        if False in assert_res:
            raise AssertionError












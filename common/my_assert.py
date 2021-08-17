# -*- coding: utf-8 -*-
# @Time     : 2021/8/1 9:54
# @Author   : lemon_zhenzhen
# @Email    :544578369@qq.com
# @file     : my_assert.py
import ast
import jsonpath
from common.my_logger import logger
from common.my_mysql import MyMysql

class MyAssert:

    def assert_requests_value(self,check_str,response_dict):
        """
        :patam check_str:从excel当中，读取出来的断言列，是一个列表形式的字符串，里面的成员是一个断言，
        :param response_dict:接口请求之后的响应数据，是字典类型
        :return:None
        """
        # 所有断言的比对结果列表
        check_res = []

        # 把字符串转换成python列表
        #check_list = eval(check_str)  # 比eval安全一点，转成列表
        check_list = eval(check_str)

        for check in check_list:
            logger.info("要断言的内容为： \n{}".format(check_list))
            # 通过jsonpath表达式，从响应结果当中拿到实际结果
            actual = jsonpath.jsonpath(response_dict, check["expr"])
            logger.info("从响应结果当中，提取到的值为： \n{}".format(actual))
            logger.info("期望结果为： \n{}".format(check["expected"]))
            if isinstance(actual, list):
                actual = actual[0]
                logger.info("从响应结果当中，提取到的值为： \n{}".format(actual))
            # 与实际结果做比对
            if check["type"] == "eq":
                logger.info("比对2个值是否相等，")
                logger.info("比对结果为： \n{}".format(actual == check["expected"]))
                check_res.append(actual == check["expected"])

        if False in check_res:
            logger.error("部分断言失败！请查看对比结果为False")
            # raise AssertionError
            return False
        else:
            logger.info("所有断言成功！")
            return True

    def assert_db(self,check_db_str):
        """
        1、将check_db_str转换python对象，通过eval，
        2、遍历1中的列表，访问每一组db比对，
        3、对于每一组来讲，1）调用数据库类，执行sql语句，调用哪个方法，根据type来决定，得到实际结果，
                        2）
        :param check_db_str: 测试数据excel当中，assert_db列读取出来的数据库校验字符串，
            示例：[{"sql":"select id from member where mobile_phone='#phone#'","expected":1,"type":"count"}]
        :return:
        """
        # 所有断言的比对结果列表
        check_db_res = []

        # 把字符串转换成python列表
        check_db_list = ast.literal_eval(check_db_str)  # 比eval安全一点，转成列表

        #建立数据库连接
        db = MyMysql()

        #遍历check_db_list
        for check_db_dict in check_db_list:
            logger.info("当前要比对的sql语句： \n{}".format(check_db_dict["sql"]))
            logger.info("当前执行sql的查询类型（查询结果条数/查询某个值）： \n{}".format(check_db_dict["db_type"]))
            logger.info("期望结果为： \n{}".format(check_db_dict["expected"]))
            #根据type来调用不同的方法执行sql语句，
            if check_db_dict["db_type"] == "count":
                logger.info("比对数据库查询的结果条数，是否符合期望")
                #执行sql语句
                res = db.get_count(check_db_dict["sql"])
                logger.info("sql的执行结果为： \n{}".format(res))
                #if check_db_dict["comp_type"] == "eq":
                    # #将比对结果添加到结果列表当中
                    # check_db_res.append(res == check_db_dict["sql"])
                #将比对结果添加到结果列表当中
                check_db_res.append(res == check_db_dict["expected"])
                logger.info("比对的结果为： \n{}".format(res == check_db_dict["expected"]))

        if False in check_db_res:
            logger.error("部分断言失败！请查看数据库对比结果为False")
            # raise AssertionError
            return False
        else:
            logger.info("所有断言成功！")
            return True

if __name__ == "__main__":
    #已经从Excel当中读取出来的字符串
    check_db_str = """[{"sql":"SELECT * FROM `city_user`.`user` where user_id='3010MVQGQKKQ'","expected":1,"db_type":"count"}]"""
    res = MyAssert().assert_db(check_db_str)
    print(res)
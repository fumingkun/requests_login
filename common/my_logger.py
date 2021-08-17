# -*- coding: utf-8 -*-
# @Time     : 2021/8/1 10:14
# @Author   : lemon_zhenzhen
# @Email    :544578369@qq.com
# @file     : my_logger.py
import logging
from logging import Logger
# from my_Conf import MyConf

class MyLogger(Logger):

    def __init__(self):
        # conf = MyConf("conf.ini")
        # file = conf.get("log","file")
        file = "api.log"
        #1、设置日志的名字，日志的收集级别
        # super().__init__(conf.get("log","name"),conf.get("log","level"))
        super().__init__("锦江在线_api",logging.INFO)

        #2、可以将日志输出到文件和控制台

        #自定义日志格式（Formatter）
        fmt_str = "(asctime)s %(name)s %(levelname)s %(filename)s [%(lineno)d] %(message)s"
        #实例化一个日志格式类
        formatter = logging.Formatter(fmt_str)

        #实例化渠道（Handle）
        #控制台（StreamHandle）
        handle1 = logging.StreamHandler()
        #设置渠道当中的日志显示格式
        handle1.setFormatter(formatter)
        #将渠道与日志收集器绑定起来
        self.addHandler(handle1)

        if file:
            #文件渠道（FileHandle）
            handle2 = logging.FileHandler(file,encoding="utf-8")
            #设置渠道当中的日志显示格式
            handle2.setFormatter(formatter)
            self.addHandler(handle2)

logger = MyLogger()

















# -*- coding: utf-8 -*-
# @Time     : 2021/8/1 17:17
# @Author   : lemon_zhenzhen
# @Email    :544578369@qq.com
# @file     : my_conf.py
from configparser import ConfigParser

class MyConf(ConfigParser):

    def __init__(self,filename):
        super().__init__()
        self.read(filename,encoding="utf-8")














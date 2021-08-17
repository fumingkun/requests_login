# -*- coding: utf-8 -*-
# @Time     : 2021/8/1 17:22
# @Author   : lemon_zhenzhen
# @Email    :544578369@qq.com
# @file     : my_path.py
import os

# 1、basedir
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 2、拼到配置文件路径
conf_dir = os.path.join(basedir,"conf")

# 3、拼接  测试数据路径
testdata_dir = os.path.join(basedir,"test_excel")

# 4、日志路径
log_dir = os.path.join(basedir,"outputs","logs")

# 5、报告路径
report_dir = os.path.join(basedir,"outputs","reports")



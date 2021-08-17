# -*- coding: utf-8 -*-
# @Time     : 2021/8/3 22:37
# @Author   : lemon_zhenzhen
# @Email    :544578369@qq.com
# @file     : 6_正则表达式.py

"""
柠檬班re相关的文章：
    https://www.cnblogs.com/Simple-Small/p/9150947.html

regular表达式学习手册：
    https://tool.oschina.net/uploads/apidocs/jquery/regexp.html
    https://gitee.com/thinkyoung/learn_regex

正则表达式： 操作对象-字符串
1、从字符串当中，提取匹配的内容

re模块
re.findall -- 返回的是列表，列表里是匹配的所有字符。

1、匹配1个字符
. 除换行符以外的所有字符  \n
\d 只匹配数字0-9
\D 匹配非数字
\w 匹配包括下划线的任何单词字符。等价于“[A-Za-z0-9_]”， 支持中文
\W 匹配任何非单词字符。等价于“[^A-Za-z0-9_]”

[a-z]   匹配小写字母
[A-Z]   匹配大写字母
[0-9]   匹配数字

[abcd]  字符集合。匹配所包含的任意一个字符。例如，“[abc]”可以匹配“plain”中的“a”
[a|b]    匹配x或y。例如，“z|food”能匹配“z”或“food”。“(z|f)ood”则匹配“zood”或“food”


2、数量匹配
*  匹配前一个字符，0次或者多次
+  匹配前一个字符，1次或者多次
?  匹配前一个字符，0次或1次

{n}   匹配前一个字符n次
{n,m}  匹配前一个字符最少是n次，最多是m次
{n,}   匹配前一个字符最少是n次，没有下限。

贪婪模式： 尽可能的匹配更多更长      对人民币贪婪，越多越好。
非贪婪模式： 尽可能的匹配更少    在数量表达后面加上？   对无偿加班时间，越少越好。

边界匹配：
^     匹配输入字符串的开始位置
$    匹配输入字符串的结束位置

匹配分组：()

"""
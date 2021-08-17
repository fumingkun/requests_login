#fumingkun
#python3.8.2
"""
python : None
java/javascript: null(python不认识。如果响应结果当中有null, 需要转换成None)
字典：数据类型。
json: 数据格式。 json格式的字符串

内置库：json
json.loads()  把json串，转换成python字典
json.dumps()  把python字典，转换成json串

关于requests处理json参数的文章：
     https://www.cnblogs.com/Simple-Small/p/9830270.html




"""
import json

req_data = '{"mobile_phone": "18610100022","pwd": "123456789","reg_name": "py37小简", "test": null}'
req_dict = json.loads(req_data)
print(type(req_dict))
print(req_dict)









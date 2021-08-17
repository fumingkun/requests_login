#fumingkun
#python3.8.2

from common.my_requests import MyRequests
import pytest

datas = [
    {"method" : "post",
     "url" : "https://ysh.visitshanghai.net/proxy/city-unity-order-data-h5-app/unity/order/user/order/list",
     "booy" : {
        "orderCategory":"",
        "pageNum":1,
        "pageSize":15,
        "tab":""
    }},
    {"method" : "post",
     "url" : "https://mall.visitshanghai.net/proxy/micro-mall-booking/queryOrder/detail",
     "booy" : {
        "platform": 1,
        "token": "2f5bb0526a3419c456ea141a43071e1921f696730e54eb7e586722493abf13c1",
        "orderNo": None,
        "subOrderNo": None
    }}
]
mr = MyRequests()
#第一种方式
# def test_api1():
#         rep = mr.send_requests(datas[0]["method"],datas[0]["url"],datas[0]["booy"])
#         print(rep.json())
# 第二种方式
# def test_api1():
#     for item in datas:
#         rep = mr.send_requests(item["method"],item["url"],item["booy"])
#         print(rep.json())
#         assert False

@pytest.mark.parametrize("item",datas)
def test_api1(item):
        rep = mr.send_requests(item["method"],item["url"],item["booy"])
        print(rep.json())
        assert False
# 一组数据就是一条用例,某一组即便运行失败了，下一组仍然会运行，


def test_api2():
    rep = mr.send_requests(datas[1]["method"],datas[1]["url"],datas[1]["booy"])
    print(rep.json())

#fumingkun
#python3.8.2

import requests
import json
import os
from common.my_logger import logger
from common.my_conf import MyConf
from common.my_path import conf_dir

class MyRequests:

    #初始化请求头
    def __init__(self):
        #请求头
    #     self.headers  = {
    #     "city-version":"1.0",
    #     "Content-Type":"application/json;charset=UTF-8",
    #     "token":"",
    #     "city-token":"",
    #     "city-nk":"MjlCRUI3MDU4QkQzNEM3QQ==",
    #     "city-language":"zh",
    #     "city-channel-code":"10009",
    #     "city-app-name":"BGSH_CHINA",
    #     "city-encrypt-enable":"false"
    # }
        self.headers = {
            "city-app-name": "BGSH_CHINA",
            "Content-Type": "application/json;charset=UTF-8",
            "city-nk": "ODFENTQyQzBDNUJCRkY2Qg==",
            "city-token":"",
            "city-language": "zh",
            "city-channel-code": "10008",
            "city-version": "1.0",
            "city-encrypt-enable": "false"
        }
        #读取配置文件当中的server地址
        self.base_url = MyConf(os.path.join(conf_dir,"conf.ini")).get("server","host")

    def send_requests(self,method,api_url,data):
        #处理请求头
        # self.__deal_header(token)

        #处理请求URL
        url = self.__deal_url(api_url)

        logger.info("请求url: \n{}".format(url))
        logger.info("请求方法: \n{}".format(method))
        logger.info("请求数据: \n{}".format(data))

        #调用requests的方法去发起一个请求，并得到响应结果
        if method.upper() == "GET":
            resp = requests.request(method,url,params=data,headers=self.headers)
        else:
            resp = requests.request(method,url,json=data,headers=self.headers)
        logger.info("响应结果: \n{}".format(resp.text))
        return resp

    def __deal_header(self,token=None):
        if token:
            self.headers["city-token"] = "{}".format(token)
            logger.info("请求为：\n{}".format(self.headers))

    def __deal_url(self,api_url):
        url = self.base_url + api_url
        return url


if __name__ == "__main__":
    my = MyRequests()

    # print(my.headers)
    a=my.headers
    a['city-token']='ODFENTQyQzBDNUJ'
    print(a)
    # my['city-token']
    #
    # #请求地址（订单列表）
    # url = "member/login/loginBySms"
    # #请求体
    # booy = {
    # "loginName": "15821894461",
    # "validateCode": "111111"
    # }
    # method = "post"
    # rep = my.send_requests(method,url,booy)
    # rep.dict = rep.json()
    # token = rep.dict["token"]
    # print(token)











    # #请求地址（订单列表）
    # url = "proxy/city-unity-order-data-h5-app/unity/order/user/order/list"
    # #请求体
    # booy = {
    #     "orderCategory":"",
    #     "pageNum":1,
    #     "pageSize":15,
    #     "tab":""
    # }
    # method = "post"
    # rep = my.send_requests(method,url,booy)
    # # print(rep.json())
    #
    # #提取数据
    # json_rew = rep.json()
    # raw_id1 = json.loads(json_rew["result"]["orderList"][0]["detail"])["orderNo"]
    # raw_id2 = json.loads(json_rew["result"]["orderList"][0]["detail"])["subOrderNo"]
    #
    # #请求地址（订单详情）
    # url = "https://mall.visitshanghai.net/proxy/micro-mall-booking/queryOrder/detail"
    # #请求体
    # booy_1 = {
    #     "platform": 1,
    #     "token": "2f5bb0526a3419c456ea141a43071e1921f696730e54eb7e586722493abf13c1",
    #     "orderNo": raw_id1,
    #     "subOrderNo": raw_id2
    # }
    # method = "post"
    # rep = my.send_requests(method,url,booy_1)
    # print(rep.json())

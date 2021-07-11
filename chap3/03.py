# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/11 9:02
# @Author  : layman
import requests

url = "https://www.baidu.com"
proxies = {"https": "218.75.158.153:3128"}
resp = requests.get(url, proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)

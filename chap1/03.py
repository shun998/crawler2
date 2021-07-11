# -*- coding: utf-8 -*-
# TODO  post
# @Date    : 2021/7/9 15:31
# @Author  : layman
import requests

url = 'https://fanyi.baidu.com/sug'
s = input("请输入要翻译的单词:")
data = {"kw": s}
resp = requests.post(url, data=data)
print(resp.json())
resp.close()
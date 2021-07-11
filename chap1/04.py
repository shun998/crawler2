# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/9 15:41
# @Author  : layman
import requests

url = 'https://movie.douban.com/j/chart/top_list'
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
# 重新封装参数
param = {"type": "24",
         "interval_id": "100:90",
         "action": "",
         "start": 20,
         "limit": 20}
resp = requests.get(url, params=param,headers=headers)
print(resp.text)
# print(resp.request.headers)
print(resp.json())
resp.close()
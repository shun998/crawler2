# -*- coding: utf-8 -*-
# TODO  客户端渲染 服务端渲染   get
# @Date    : 2021/7/9 15:02
# @Author  : layman
import requests

query = input("输入搜索的内容:")
url = f'https://www.sogou.com/web?query={query}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
resp = requests.get(url, headers=headers)
print(resp)
print(resp.text)
resp.close()
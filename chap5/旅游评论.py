# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/15 18:22
# @Author  : layman
import requests

url = 'https://www.yichangly.com/tour/show-8.html'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
resp = requests.get(url, headers=headers)
# print(resp.text)
url_comm = 'https://www.yichangly.com/api/comment.php?mid=22&itemid=8'
print(requests.get(url_comm, headers=headers).text)

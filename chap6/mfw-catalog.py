# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/16 11:09
# @Author  : layman
import csv
import re

import requests

url = 'http://www.mafengwo.cn/localdeals/ajax_2017.php'
params = {"act": "GetContentList",
          "from": "NaN",
          "to": "M10490",
          "salesType": "NaN",
          "page": "1",
          "group": "NaN",
          "sort": "smart",
          "sort_type": "desc",
          "limit": "20"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
resp = requests.get(url, params=params, headers=headers)
resp.encoding = "UTF-8"
# print(resp.json())
dic = resp.json()
# with open('catalog.json', 'w', encoding='utf-8') as f:
#     f.write(repr(dic))
# f.close()
li = dic['html']['list']
total_page = dic['msg']['total']
print(total_page)
obj1 = re.compile(
    r'.*?<a class="item clearfix" href="(?P<href>.*?)" target="_blank">.*?<h3>(?P<title>.*?)</h3>',
    re.S)
f = open("马蜂窝链接.csv", mode="a", encoding="utf-8")
csv_writer = csv.writer(f)
result = obj1.finditer(li)
for i in result:
    sales_id = i.group('href').strip().split('/')[-1].split('.')[0]
    title = i.group('title').strip()
    print(sales_id, title)
    csv_writer.writerow([sales_id,title])

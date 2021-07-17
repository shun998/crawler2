# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/16 10:23
# @Author  : layman
import csv
import json
import re

import requests

url = 'http://www.mafengwo.cn/sales/c/comment/api/list'
params = {"star": "0",
          "has_img": '',
          "page_no": "1",
          "style": "html",
          "decorate": "www",
          "sales_id": "6767341"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
resp = requests.get(url, params=params, headers=headers)
resp.encoding = "UTF-8"
dic = resp.json()
# with open('com.json', 'w', encoding='utf-8') as f:
#     f.write(repr(dic))
# f.close()
li_list = dic['data']['list']
total_num=dic['data']['page']['data_total']
print(total_num)
# obj1 = re.compile(
#     r'<li class="rev-item">.*?<p class="txt">(?P<comment>.*?)</p>.*?<span class="time">(?P<time>.*?)</span>', re.S)
# f = open("马蜂窝评论-copy.csv", mode="a", encoding="utf-8")
# csv_writer = csv.writer(f)
# for li in li_list:
#     result = obj1.finditer(li)
#     for i in result:
#         # comment = i.group('comment')
#         # time = i.group('time')
#         j = i.groupdict()
#         csv_writer.writerow(j.values())

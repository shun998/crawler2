# -*- coding: utf-8 -*-
# TODO  获得top250第一条数据
# @Date    : 2021/7/9 16:25
# @Author  : layman
import re
import csv

import requests

url = 'https://movie.douban.com/top250'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
resp = requests.get(url, headers=headers)
page_content = resp.text
# 解析数据
obj = re.compile(
    r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>',
    re.S)
result = obj.finditer(page_content)
f = open("doubantop250-1.csv", mode="w", encoding="utf-8")
csv_writer = csv.writer(f)
for i in result:
    # print(i.group("name"))
    # print(i.group("year").strip())
    # print(i.group("score"))
    # print(i.group("num"))
    dic = i.groupdict()
    dic['year'] = dic['year'].strip()
    csv_writer.writerow(dic.values())
f.close()
print('over!')

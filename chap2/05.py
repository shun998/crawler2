# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/10 12:31
# @Author  : layman
import csv
import re

import requests

domain = "https://www.dy2018.com/"
resp = requests.get(domain)
resp.encoding = "gb2312"  # 指定字符集
# print(resp.text)
obj1 = re.compile(r'2021必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(
    r'<div class="title_all"><h1>.*?《(?P<title>.*?)》.*?</h1></div>.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)
result1 = obj1.finditer(resp.text)
child_list = []
f = open("dytt2018.csv", mode="a", encoding="utf-8")
csv_writer = csv.writer(f)
for i in result1:
    ul = i.group("ul")
    # print(ul)
    result2 = obj2.finditer(ul)
    for i in result2:
        href = i.group("href")
        # print(href)
        child_href = domain + href.strip("/")
        child_list.append(child_href)
for href in child_list:
    child_resp = requests.get(href)
    child_resp.encoding = "gb2312"  # 指定字符集
    result3 = obj3.finditer(child_resp.text)
    for i in result3:
        # title = i.group("title")
        # download = i.group("download")
        # print(title)
        # print(download)
        dic = i.groupdict()
        csv_writer.writerow(dic.values())

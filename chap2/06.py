# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/10 14:25
# @Author  : layman
import csv

import requests
from bs4 import BeautifulSoup

url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp = requests.get(url)
f = open("菜价.csv", mode="w", encoding="utf-8")
csv_writer = csv.writer(f)
# print(resp.text)
page = BeautifulSoup(resp.text, "html.parser")
# table = page.find("table", class_="hq_table")  # class是pythoon的关键字
table = page.find("table", attrs={"class": "hq_table"})
# print(table)
trs = table.find_all("tr")[1:]
for tr in trs:
    tds = tr.find_all("td")
    name = tds[0].text
    low = tds[1].text
    average = tds[2].text
    high = tds[3].text
    standard = tds[4].text
    cell = tds[5].text
    date = tds[6].text
    # print(name, low, average, high, standard, cell, date)
    csv_writer.writerow([name, low, average, high, standard, cell, date])
f.close()
print("over!")

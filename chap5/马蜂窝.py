# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/14 20:41
# @Author  : layman

import requests
from lxml import etree

url = "http://www.mafengwo.cn/localdeals/0-0-M10490-0-0-0-0-0.html?_t=1626328770798"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
resp = requests.get(url, headers=headers)
resp.encoding = "UTF-8"
# print(resp.text)
html = etree.HTML(resp.text)
div = html.xpath('/html/body/div[2]/div[2]')[0]
p = div.xpath('./div[4]/a/div[2]/div//text()')[0].strip()
print(p)

# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/10 15:53
# @Author  : layman
import requests
from lxml import etree

url = "https://yichang.zbj.com/search/f/?type=new&kw=saas"
resp = requests.get(url)
# print(resp.text)
html = etree.HTML(resp.text)
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[*]/div/div")
for div in divs:
    price = div.xpath("./a[1]/div[2]/div[1]/span[1]/text()")[0].strip("¥")
    title = "saas".join(div.xpath("./a[1]/div[2]/div[2]/p/text()"))
    com_name = div.xpath("./a[2]/div[1]/p/text()")[1]
    print(price, title, com_name)

# -*- coding: utf-8 -*-
# TODO  北京新发地爬虫
# @Date    : 2021/7/11 12:57
# @Author  : layman
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

import csv

f = open("菜价.csv", encoding="utf-8", mode="a")
csv_writer = csv.writer(f)


def download_one_page(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    # print(resp.text)
    html = etree.HTML(resp.text)
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    trs = table.xpath("./tr")[1:]
    # trs = table.xpath("./tr[position()>1]")
    for tr in trs:
        txt = tr.xpath("./td/text()")
        txt = (item.replace("\\", "").replace("/", "") for item in txt)
        # print(list(txt))
        csv_writer.writerow(txt)
    resp.close()
    print(url, "文件提取完毕")


if __name__ == '__main__':
    # download_one_page("http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml")
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            t.submit(download_one_page, f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")
    print("全部下载完毕!")

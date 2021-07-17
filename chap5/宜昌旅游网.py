# -*- coding: utf-8 -*-
# TODO  爬取宜昌旅游网评论
# @Date    : 2021/7/15 16:57
# @Author  : layman
import re

import requests
from lxml import etree

#
# url = f"https://www.yichangly.com/tour/search-htm-catid-0-kw--areaid-203-page-{page}.html"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
# resp = requests.get(url, headers=headers)
obj1 = re.compile(
    r'.*?<li class="newborder ">.*?<a href="(?P<href>.*?)".*?target="_blank" title="(?P<title>.*?)".*?<i class="sign">￥</i>(?P<price>.*?)<i class="unit">/人</i>',
    re.S)
# result = obj.finditer(resp.text)
# for i in result:
#     print(i.group('href'), i.group('title').replace('&lt;', '').replace('&gt;', ''), i.group('price'))


obj1 = re.compile(
    r'.*?<li class="newborder ">.*?<a href="(?P<href>.*?)".*?target="_blank" title="(?P<title>.*?)".*?<i class="sign">￥</i>(?P<price>.*?)<i class="unit">/人</i>',
    re.S)
obj2 = re.compile(
    r'.*?<h1>(?P<title>.*?)</h1>.*?<dd style="width:80px; text-align:left; margin-left:0px; float:left;"><strong class="forg">(?P<price>.*?)</strong>.*?<dd>(?P<address>.*?)<a href="#a2" class="maplink"><i class="fa fa-location-arrow mr5"></i>查看地图</a></dd>',
    re.S)


def download_page(page):
    child_href_list = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

    for i in range(1, page):
        url = f"https://www.yichangly.com/tour/search-htm-catid-0-kw--areaid-203-page-{page}.html"
        resp = requests.get(url, headers=headers)
        result = obj1.finditer(resp.text)
        for i in result:
            href = i.group('href')
            child_href_list.append(href)
            # title=i.group('title').replace('&lt;', '').replace('&gt;', '')
            # price=i.group('price')
            # print(i.group('href'), i.group('title').replace('&lt;', '').replace('&gt;', ''), i.group('price'))
        for href in child_href_list:
            headers = {
                "Cookie": "ab_jid=e4c26bcdaae3c8c96e057ba91b8393c3493e; ab_jid_BFESS=e4c26bcdaae3c8c96e057ba91b8393c3493e; BDUSS_BFESS=XZUSEdTVEVMSUVSckd6M3hNeVl4bVdMNENLSzR2d204NElaUnRmMjB0cER4UHRnRVFBQUFBJCQAAAAAAAAAAAEAAACjiR6mwMvAy7Tz1~fVvQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEM31GBDN9RgQ; BAIDUID_BFESS=CDF79A4D5ED7B947EC8C9B3AEFA44194:FG=1; ab_bid=977c7d21b92f5ccf374776fcf2d6b45dbf9c; ab_sr=1.0.1_ZDYyYmRlMGNjZWQ5MDJmNzEwYWUwZTdmYjNiZDc0MjU0MjcwNzEwMGI1MDE1MmI3OTMxMWQ3ZWQ5NzE4NWFjMTVmOGRjNzBhNmFmYjJkNDY2NzI5NDYzNDJkMGY5ZTc4MWQ1Mzc1MjQyZjVhZjYyMTJkOTNjOWVjOWQzZmMxYjgyNTkwNzIxYjBkOGI1ZTU3OGQxZTZmOGRiMTJhZWEzNw==",
                "Host": "miao.baidu.com",
                "Origin": "https://www.yichangly.com",
                "Pragma": "no-cache",
                "Referer": "https://www.yichangly.com/",
                # "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                # "sec-ch-ua-mobile": "?0",
                # "Sec-Fetch-Dest": "empty",
                # "Sec-Fetch-Mode": "cors",
                # "Sec-Fetch-Site": "cross-site",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
            child_resp = requests.get(href, headers=headers)
            result2 = obj2.finditer(child_resp.text)
            for i in result2:
                print(i.group('title'), i.group('price'), i.group('address'))


# def download_childpage():
download_page(5)

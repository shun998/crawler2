# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/16 12:28
# @Author  : layman
import csv
import random
import re
import time

import requests

user_agent_list = [
    # Opera
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    "Opera/8.0 (Windows NT 5.1; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
    # Firefox
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    # Safari
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    # chrome
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    # 360
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    # 淘宝浏览器
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    # 猎豹浏览器
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    # QQ浏览器
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    # sogou浏览器
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
    # maxthon浏览器
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    # UC浏览器
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
]
ip_list = ['113.237.3.178:9999', "118.117.188.171:3256", "104.254.238.122:20171", "185.179.30.130:8080",
           "178.134.208.126:50824", "175.42.122.142:9999","182.84.144.91:3256","167.172.180.46:33555"]


def download_catalog(url):
    url = 'http://www.mafengwo.cn/localdeals/ajax_2017.php'
    params = {"act": "GetContentList",
              "from": "NaN",
              "to": "M10490",
              "salesType": "NaN",
              "page": 1,
              "group": "NaN",
              "sort": "smart",
              "sort_type": "desc",
              "limit": "20"}
    headers = {
        "User-Agent":random.choice(user_agent_list)}
    resp = requests.get(url, params=params, headers=headers)
    resp.encoding = "UTF-8"
    dic = resp.json()
    li = dic['html']['list']
    total_num = dic['msg']['total']
    obj1 = re.compile(
        r'.*?<a class="item clearfix" href="(?P<href>.*?)" target="_blank">.*?<h3>(?P<title>.*?)</h3>',
        re.S)
    # 此处的total_page暂时不用
    sales_id_list = []
    title_list = []
    f = open("马蜂窝旅游项目2.csv", mode="a", encoding="utf-8")
    csv_writer = csv.writer(f)
    for page_num in range(1, (total_num + 20 - 1) // 20 + 1):
        params["page"] = page_num
        ip_proxy = {"http": random.choice(ip_list)}
        headers = {
            "User-Agent": random.choice(user_agent_list)}
        resp = requests.get(url, params=params, headers=headers,proxies=ip_proxy)
        result = obj1.finditer(li)
        for i in result:
            sales_id = i.group('href').strip().split('/')[-1].split('.')[0]
            title = i.group('title').strip()
            sales_id_list.append(sales_id)
            csv_writer.writerow([sales_id, title])
    print("项目列表over")
    return sales_id_list


def download_comment(sales_id):
    url = 'http://www.mafengwo.cn/sales/c/comment/api/list'
    params = {"star": "0",
              "has_img": '',
              "page_no": "1",
              "style": "html",
              "decorate": "www",
              "sales_id": f"{sales_id}"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
    resp = requests.get(url, params=params, headers=headers)
    resp.encoding = "UTF-8"
    dic = resp.json()
    li_list = dic['data']['list']
    total_num = dic['data']['page']['data_total']
    obj1 = re.compile(
        r'<li class="rev-item">.*?<p class="txt">(?P<comment>.*?)</p>.*?<span class="time">(?P<createTime>.*?)</span>',
        re.S)
    f = open("马蜂窝评论2.csv", mode="a", encoding="utf-8")
    csv_writer = csv.writer(f)
    for page_no in range(1, (total_num + 10 - 1) // 10 + 1):
        params["page_no"] = page_no
        ip_proxy = {"http": random.choice(ip_list)}
        headers = {
            "User-Agent": random.choice(user_agent_list)}
        resp = requests.get(url, params=params, headers=headers,proxies=ip_proxy)
        resp.encoding = "UTF-8"
        for li in li_list:
            result = obj1.finditer(li)
            for i in result:
                createTime = i.group("createTime")
                comment = i.group("comment")
                csv_writer.writerow([sales_id, createTime, comment])
    print('评论over!')


if __name__ == '__main__':
    sales_id_list = download_catalog('http://www.mafengwo.cn/localdeals/ajax_2017.php')
    for sales_id in sales_id_list:
        download_comment(sales_id)
    print('finish!')

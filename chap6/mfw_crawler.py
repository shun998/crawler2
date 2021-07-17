# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/16 12:28
# @Author  : layman
import csv
import re

import requests


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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
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
    f = open("马蜂窝旅游项目.csv", mode="a", encoding="utf-8")
    csv_writer = csv.writer(f)
    for page_num in range(1, (total_num + 20 - 1) // 20 + 1):
        params["page"] = page_num
        resp = requests.get(url, params=params, headers=headers)
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
        r'<li class="rev-item">.*?<p class="txt">(?P<comment>.*?)</p>.*?<span class="time">(?P<time>.*?)</span>', re.S)
    f = open("马蜂窝评论.csv", mode="a", encoding="utf-8")
    csv_writer = csv.writer(f)
    for page_no in range(1, (total_num + 10 - 1) // 10 + 1):
        params["page_no"] = page_no
        resp = requests.get(url, params=params, headers=headers)
        resp.encoding = "UTF-8"
        for li in li_list:
            result = obj1.finditer(li)
            for i in result:
                time = i.group("time")
                comment = i.group("comment")
                csv_writer.writerow([sales_id, time, comment])
    print('评论over!')


if __name__ == '__main__':
    sales_id_list = download_catalog('http://www.mafengwo.cn/localdeals/ajax_2017.php')
    for sales_id in sales_id_list:
        download_comment(sales_id)
    print('finish!')

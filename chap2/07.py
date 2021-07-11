# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/10 14:50
# @Author  : layman
import time

import requests
from bs4 import BeautifulSoup

url = "https://www.umei.net/bizhitupian/"
resp = requests.get(url)
resp.encoding = "utf-8"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
# print(resp.text)
main_page = BeautifulSoup(resp.text, "html.parser")
a_list = main_page.find("div", class_="TypeList").find_all("a")
# print(a_list)
for a in a_list:
    # print(a.get("href"))
    href = "https://www.umei.net" + a.get("href")

    child_resp = requests.get(href)
    child_resp.encoding = "utf-8"
    child_resp_text = child_resp.text
    child_page = BeautifulSoup(child_resp_text, "html.parser")
    p = child_page.find("p", align="center")
    img = p.find("img")
    # print(img.get("src"))
    src = img.get("src")
    img_resp = requests.get(url=src, headers=headers)
    img_name = src.split("/")[-1]
    with open("img/" + img_name, mode="wb") as f:
        f.write(img_resp.content)
    print("over~", img_name)
    time.sleep(1)
print("all over~")

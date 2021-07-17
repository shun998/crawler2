# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/15 10:16
# @Author  : layman
import requests

url = 'https://s.weibo.com/Ajax_Comment/small'
data = {"ajwvr": 6,
        "act": "list",
        "mid": 4488864263366250,
        "uid": 7327791612,
        "isMain": "true",
        "dissDataFromFeed": "[object Object]",
        "ouid": 6403816954,
        "location": "page_100606_home",
        "comment_type": 0,
        "_t": 0,
        "__rnd": "1626316186640"}
headers = {"Referer": "https://s.weibo.com/weibo?Refer=top",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
           "X-Requested-With": "XMLHttpRequest"
           ,"referer": "https://weibo.com/leetcodecn?from=myfollow_no-group&is_all=1",
           "cookie": "SINAGLOBAL=5440304095393.5.1598179212753; _s_tentry=www.baidu.com; UOR=www.baidu.com,open.weibo.com,www.baidu.com; Apache=9524650653437.662.1626314245221; ULV=1626314245294:1:1:1:9524650653437.662.1626314245221:; SSOLoginState=1626314445; SUB=_2A25N6-acDeRhGeFN6VUW-S_Kyj6IHXVvF4rUrDV8PUJbkNAKLWbHkW1NQFh55mjnP6rYNKbzfoM6nY9lkiHSLpK9; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF4kv-4n5KEAdq3XeiQfdqc5NHD95QNe0zNS0.pSo2EWs4DqcjiqJLrds84dg8V; wvr=6; wb_view_log_7327791612=1536*8641.25; webim_unReadCount=%7B%22time%22%3A1626316182866%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A38%2C%22msgbox%22%3A0%7D"}
resp = requests.post(url, data=data, headers=headers)
print(resp.json())

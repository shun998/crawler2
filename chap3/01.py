# -*- coding: utf-8 -*-
# TODO  两种方式登录 session or cookie
# @Date    : 2021/7/10 16:54
# @Author  : layman
import requests

# session = requests.session()
# url = "https://passport.17k.com/ck/user/login"
# data = {"loginName": "18827262101",
#         "password": "dsgzs=0818"}
# session.post(url=url, data=data)
# # print(resp.text)
# # print(resp.cookies)
# resp = session.get("https://user.17k.com/ck/user/mine/readList?page=1&appKey=2406394919")
# print(resp.json())
resp2 = requests.get("https://user.17k.com/ck/user/mine/readList?page=1&appKey=2406394919", headers={
    "Cookie": "GUID=bc41f522-a1a8-46ad-860a-c9c4cd8cd293; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F01%252F41%252F97%252F78109741.jpg-88x88%253Fv%253D1625907409000%26id%3D78109741%26nickname%3Dshun998%26e%3D1641459518%26s%3D9433bea554fe73bf; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2278109741%22%2C%22%24device_id%22%3A%2217a8fa15ddb8e1-04ec546aa7ddbd-f7f1939-1327104-17a8fa15ddc692%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22bc41f522-a1a8-46ad-860a-c9c4cd8cd293%22%7D"})
print(resp2.json())

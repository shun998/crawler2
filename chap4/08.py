# -*- coding: utf-8 -*-
# TODO  爬取西游记小说
# @Date    : 2021/7/11 15:26
# @Author  : layman
# url='https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}' 先有这个cid,再获取下面的连接
# url='https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}'
import json

import aiofiles
import requests
import aiohttp
import asyncio

"""
同步获取catalog
异步获取content
"""


async def get_catalog(url):
    resp = requests.get(url)
    # print(resp.json())
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        tasks.append(aiodownload(cid, b_id, title))
    await asyncio.wait(tasks)
    # print(title, cid)


async def aiodownload(cid, b_id, title):
    data = {"book_id": b_id, "cid": f"{b_id}|{cid}", "need_bookinfo": 1}
    data = json.dumps(data)
    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    async with aiohttp.ClientSession() as  session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open("novel/" + title + ".txt", mode="w", encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])


if __name__ == '__main__':
    b_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + b_id + '"}'
    asyncio.run(get_catalog(url))

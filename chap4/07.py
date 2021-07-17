# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/11 14:37
# @Author  : layman
import asyncio
import aiohttp

urls = ["http://kr.shanghai-jiuxin.com/file/2021/0709/e2cf7fb09c9f896bb5dbc0d3b83b403b.jpg",
        "http://kr.shanghai-jiuxin.com/file/2021/0709/d41f22ef341fdabe32abad4e454bc2a1.jpg",
        "http://kr.shanghai-jiuxin.com/file/2021/0709/9369a6b0084ceca4640c2e3c61f02731.jpg"]


async def aiodownload(url):
    name = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open("img/" + name, mode="wb") as f:
                f.write(await resp.content.read())


async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())

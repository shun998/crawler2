# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/11 14:01
# @Author  : layman
import asyncio

# async def func():
#     print("我是憨八龟")
#
#
# if __name__ == '__main__':
#     g = func()
#     asyncio.run(g)
import time


# async def func1():
#     print("我是野原新之助")
#     # time.sleep(3)
#     await asyncio.sleep(3)
#     print("我是野原新之助")
#
#
# async def func2():
#     print("我是野原广志")
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("我是野原广志")
#
#
# async def func3():
#     print("我是小山美伢")
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print("我是小山美伢")
#
#
# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [f1, f2, f3]
#     t1 = time.time()
#     asyncio.run(asyncio.wait(tasks))
#     t2 = time.time()
#     print(t2 - t1)

async def func1():
    print("我是野原新之助")
    # time.sleep(3)
    await asyncio.sleep(3)
    print("我是野原新之助")


async def func2():
    print("我是野原广志")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("我是野原广志")


async def func3():
    print("我是小山美伢")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("我是小山美伢")


async def main():
    # f1=func1()
    # await f1
    tasks = [asyncio.create_task(func1()), asyncio.create_task(func2()), asyncio.create_task(func3())]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)

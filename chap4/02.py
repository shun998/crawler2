# -*- coding: utf-8 -*-
# TODO  多进程
# @Date    : 2021/7/11 12:41
# @Author  : layman
from multiprocessing import Process


def func(name):
    for i in range(10000):
        print(f"{name}------", i)


if __name__ == '__main__':
    p = Process(target=func,args=("Jack",))
    p.start()
    p2 = Process(target=func, args=("HH",))
    p2.start()
    for i in range(10000):
        print("主进程~~~~", i)

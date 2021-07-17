# -*- coding: utf-8 -*-
# TODO  多线程
# @Date    : 2021/7/11 12:29
# @Author  : layman
# def func():
#     for i in range(100):
#         print("func", i)
#
#
# if __name__ == '__main__':
#     func()
#     for i in range(100):
#         print("main", i)
# 多线程
from threading import Thread


# def func():
#     for i in range(100):
#         print("func", i)
#
#
# if __name__ == '__main__':
#     t = Thread(target=func)
#     t.start()
#     for i in range(100):
#         print("main", i)
class MyThread(Thread):
    def run(self):
        for i in range(100):
            print("子线程",i)
if __name__ == '__main__':
    t=MyThread()
    t.start()
    # t.run()#单线程
    for i in range(100):
        print("主线程",i)
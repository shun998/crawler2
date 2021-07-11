# -*- coding: utf-8 -*-
# TODO  re模块
# @Date    : 2021/7/9 16:02
# @Author  : layman
import re

# 获取列表,使用group()获取元素
lst = re.findall(r"\d+", "我的电话是:10086,我对象的电话是:10010")
print(lst)
# 获取迭代器,使用group()获取元素
it = re.finditer(r"\d+", "我的电话是:10086,我对象的电话是:10010")
for i in it:
    print(i.group())
# 获取match,使用group()获取元素,只能获取一个
s = re.search(r"\d+", "我的电话是:10086,我对象的电话是:10010")
print(s.group())
# 从头开始匹配
s = re.match(r"\d+", "10086,我对象的电话是:10010")
print(s.group())
# 预加载正则表达式
obj = re.compile(r"\d+")
it = obj.finditer("我的电话是:10086,我对象的电话是:10010")
for i in it:
    print(i.group())

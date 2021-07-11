# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/9 16:16
# @Author  : layman
import re

s = """
<div class='aa'><span id='1'>郭麒麟</span></div>
<div class='bb'><span id='2'>宋轶</span></div>
<div class='cc'><span id='3'>范思哲</span></div>
<div class='dd'><span id='4'>大聪明</span></div>
"""
# S让.可以匹配换行符
# (?P<组名>正则) 可以从正则的内容中提取内容
obj = re.compile(r"<div class='.*?'><span id='(?P<ii>.*?)'>(?P<jj>.*?)</span></div>", re.S)
result = obj.finditer(s)
for it in result:
    print(it.group("ii"))
    print(it.group("jj"))

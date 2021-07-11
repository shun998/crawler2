# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/10 15:36
# @Author  : layman
from lxml import etree

xml = """
<book>
<id>1</id>
<name>野花遍地香</name>
<price>1.23</price>
<nick>臭豆腐</nick>
<author>
<nick id="10086">周大强</nick>
<nick id="10010">周芷若</nick>
<nick class="joy">周杰伦</nick>
<nick class="jolion">蔡依林</nick>
<div>
<nick>惹了1</nick>
</div>
<div>
<nick>惹了2</nick>
</div>
<div>
<nick>惹了3</nick>
</div>
<span>
<nick>惹了4</nick>
</span>
</author>
<partner>
<nick id="ppc">碰碰车</nick>
<nick id="ppbc">跑跑步从</nick>
</partner>
</book>
"""
tree = etree.XML(xml)
# result = tree.xpath("/book")  #
# result = tree.xpath("/book/name")  #
# result = tree.xpath("/book/name/text()")  # 获取文本text()
# result = tree.xpath("/book/author/nick/text()")  # 获取文本text()
# result = tree.xpath("/book/author/div/nick/text()")  # 获取文本text()
result = tree.xpath("/book/author//nick/text()")  # 后代
print(result)

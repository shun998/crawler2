# -*- coding: utf-8 -*-
# TODO
# @Date    : 2021/7/16 15:01
# @Author  : layman
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.mafengwo.cn/localdeals/0-0-M10490-0-0-0-0-0.html')
browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/a[1]/div[2]/div[1]/h3').click()

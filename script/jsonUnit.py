#!/usr/bin/python3
# coding=utf-8
import re
import urllib.request
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str: str = json.dumps(data)

print(json_str)

json_data = json.loads(json_str)

print(json_data["name"])

print(json_data["url"])




def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('gb2312')
    return html


def view_stock(stock_code):
    ssl._create_default_https_context = ssl._create_unverified_context
    url = "http://hq.sinajs.cn/list=%s" % stock_code
    resp = getHtml(url)
    data = resp.split(",")
    for i in range(len(data)):
        if i == 0:
            print(data[i][21:50])
        elif i == 1:
            print("今日开盘价:", data[i])
        elif i == 2:
            print("昨日收盘价:", data[i])
        elif i == 3:
            print("当前价格:", data[i])
        elif i == 4:
            print("今日最高价:", data[i])
        elif i == 5:
            print("今日最低价:", data[i])


stock_list = ["sz000063", "sh000036", "sh000063", "sz000036"]

for i in range(len(stock_list)):
    print("=========================================================")
    view_stock(stock_list[i])

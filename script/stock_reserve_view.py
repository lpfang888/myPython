#!/usr/bin/python3
# coding=utf-8
import urllib.request
import config_operate


def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('gb2312')
    return html


def view_stock(stock_code):
    url = "http://hq.sinajs.cn/list={}".format(stock_code)
    resp = get_html(url)
    str_array = resp.split(",")
    for number in range(len(str_array)):
        if number == 0:
            print(str_array[number][21:50])
        elif number == 1:
            print("今日开盘价:", str_array[number])
        elif number == 2:
            print("昨日收盘价:", str_array[number])
        elif number == 3:
            print('[当前价格]:\033[1;35m %s \033[0m' % str_array[number])
        elif number == 4:
            print("今日最高价:", str_array[number])
        elif number == 5:
            print("今日最低价:", str_array[number])
    a = float(str_array[2])
    b = float(str_array[3])
    c = ((b - a) / a) * 100
    print("[今日跌涨]:%.2f" % c, "%")
    return str_array[3]


stock_list = config_operate.reserve_list.split(',')

for i in range(len(stock_list)):
    print("=========================================================")
    current_price = view_stock(stock_list[i])

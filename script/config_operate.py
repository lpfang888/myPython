#!/usr/bin/python3
# coding=utf-8

import configparser

# 初始化类
config = configparser.ConfigParser()
config.read("../config/stock.ini")

stock_url = config.get('stock_base', 'stock_url')
stock_code = config.get('stock_base', 'stock_code')
stock_list = config.get('stock_base', 'stock_list')
buy_price = config.get('stock_base', 'buy_price')
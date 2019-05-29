#!/usr/bin/python3
# coding=utf-8


capital = float(input("请输入你的本金："))
rate = float(input("请输入你的年利率："))
year = int(input("请输入年限："))
year_amount = float(input("请输入每月新增额度："))

total_amount = 0
for i in range(year):
    total_amount = capital * (1 + rate / 100.00) + year_amount * 12
    capital = total_amount

print("本息合计：{0}".format(round(total_amount, 2)))

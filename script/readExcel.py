#!/usr/bin/python3
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple

# 文件路径
path = '/Users/fangliangpei/fanglp/test.xlsx'

# 打开excel
workbook = xlrd.open_workbook(path)
# 输出Excel文件中所有sheet的名字
print(workbook.sheet_names())
# 获取数据sheet
data_sheet = workbook.sheet_by_name("Sheet1")

rowsnum = data_sheet.nrows;
colsnum = data_sheet.ncols;

print(rowsnum)
print(colsnum)

for i in range(rowsnum):
    fund_code = ''
    trade_type = 0
    trade_date = ''
    amount = 0.00
    price = 0.0000
    share = 0.00
    if i == 0:
        continue
    for j in range(colsnum):
        cell_value = data_sheet.cell_value(i, j)
        if j == 0:
            date = datetime(*xldate_as_tuple(cell_value, 0))
            trade_date = date.strftime('%Y-%d-%m')
        if j == 1:
            if cell_value == '买入':
                trade_type = 1
            else:
                trade_type = 2
        if j == 2:
            fund_code = int(cell_value)
        if j == 4:
            amount = str(cell_value)
        if j == 5:
            share = str(cell_value)
        if j == 6:
            price = str(cell_value)

    print("({0},{1},{2},{3},{4},{5}),".format(fund_code, trade_type, trade_date, amount, price, share))

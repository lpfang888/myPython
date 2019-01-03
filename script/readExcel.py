#!/usr/bin/python3
import xlrd

# 文件路径
path = '/Users/fangliangpei/fanglp/test.xls'

# 打开excel
workbook = xlrd.open_workbook(path)
# 输出Excel文件中所有sheet的名字
print(workbook.sheet_names())
# 获取数据sheet
data_sheet = workbook.sheet_by_name("demo")

rowsnum = data_sheet.nrows;
colsnum = data_sheet.ncols;

print(rowsnum)
print(colsnum)

cell_A1 = data_sheet.cell(0, 0).value
cell_A2 = data_sheet.cell(1, 0).value
cell_A3 = data_sheet.cell(2, 0).value
cell_B1 = data_sheet.cell(0, 1).value
cell_B2 = data_sheet.cell(1, 1).value
cell_B3 = data_sheet.cell(2, 1).value
cell_C1 = data_sheet.cell(0, 2).value
cell_C2 = data_sheet.cell(1, 2).value
cell_C3 = data_sheet.cell(2, 2).value

print(cell_A1, cell_B1, cell_C1)
print(cell_A2, cell_B2, cell_C2)
print(cell_A3, cell_B3, cell_C3)

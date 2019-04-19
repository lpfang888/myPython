#!/usr/bin/python3
import xlrd

# 文件路径
path = '/Users/fangliangpei/Downloads/cust_test.xlsx'

# 打开excel
workbook = xlrd.open_workbook(path)
# 输出Excel文件中所有sheet的名字
print(workbook.sheet_names())
# 获取数据sheet
data_sheet = workbook.sheet_by_name("test")

rowsnum: int = data_sheet.nrows
colsnum = data_sheet.ncols

print(rowsnum)
print(colsnum)

cell_A1 = data_sheet.cell(0, 0).value

insert_sql: str = """insert into t_visit_cust_duty (cust_id, cust_name, duty_user_code) values (%d,'%s','%.f');"""

for i in range(0, rowsnum):
    if i == 0:
        continue
    for j in range(0, colsnum):
        if j > 5:
            cell_value = str(data_sheet.cell(i, j).value)
            if len(cell_value) > 0:
                print(insert_sql % (
                    data_sheet.cell(i, 0).value, data_sheet.cell(i, 4).value, float(cell_value)))

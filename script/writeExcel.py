#!/usr/bin/python3
import xlwt

# 路径
path = '/Users/fangliangpei/fanglp/test.xls'


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height

    style.font = font
    return style


def write_excel(path):
    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建sheet
    data_sheet = workbook.add_sheet("demo")

    row0 = ["姓名", "性别", "年龄"]
    row1 = ["张三", "男", 21]
    row2 = ["李四", "女", 28]

    # 生成数据
    for i in range(len(row0)):
        data_sheet.write(0, i, row0[i], set_style('Times New Roman', 220, True))
        data_sheet.write(1, i, row1[i], set_style('Times New Roman', 220, True))
        data_sheet.write(2, i, row2[i], set_style('Times New Roman', 220, True))
    workbook.save(path)
    print("创建excel成功")


write_excel(path)

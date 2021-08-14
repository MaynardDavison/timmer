#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 18:04
# @Author  : hanyou
# @Software: PyCharm
"""
生成表格
"""

from docx import Document
from docx.enum.section import WD_SECTION_START, WD_ORIENTATION
import os

from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml.ns import qn
from docx.shared import RGBColor, Pt, Cm
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT  #重点


document = Document()

# 转横向
section = document.sections[0]  # 第一页设置横向
# section = document.add_section(start_type=WD_SECTION_START.CONTINUOUS) # 添加横向页的连续节，多加一页
new_width, new_height = section.page_height, section.page_width
section.orientation = WD_ORIENTATION.LANDSCAPE  # 设置横向
section.page_width = new_width  # 设置宽高后才可
section.page_height = new_height

# 设置页边距
section.top_margin = Cm(0.58)
section.bottom_margin = Cm(1.18)
section.left_margin = Cm(1.54)
section.right_margin = Cm(1.54)

# 设置字体颜色等
document.styles['Normal'].font.name = u'宋体'
document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')  # 与上面合起来才有效果
document.styles['Normal'].font.size = Pt(10.5)  # 五号
document.styles['Normal'].font.color.rgb = RGBColor(0, 0, 0)

# 添加表头
# document.add_heading('二零二一年八月上',1)#这里要改成自动生成，1代表标题1
p = document.add_paragraph()
head_line = p.add_run('二零二一年八月上')
head_line.font.size = Pt(22)  # 二号
head_line.font.name = u'黑体'  # 单独设置headline的字体
head_line._element.rPr.rFonts.set(qn('w:eastAsia'), u'黑体')
p.paragraph_format.alignment = WD_TABLE_ALIGNMENT.CENTER  # 居中
head_line.bold = True  # 字体加粗

# 添加表格
table = document.add_table(rows=16, cols=13, style='Table Grid')  # 16行13列,正常样式
# table.cell(0, 0).merge(table.cell(2, 2))  可以合并单元格

# 设置列宽
cols_width_list = [2.13, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 2.13]
for i in range(13):
    table.cell(0, i).width = Cm(cols_width_list[i])

# 设置行高
for i in range(14):#最后一行与第一行单独设置16-2
    table.rows[i+1].height = Cm(0.9)
table.rows[0].height = Cm(1)
table.rows[15].height = Cm(2.82)

# 垂直居中对其
# table.alignment = WD_TABLE_ALIGNMENT.CENTER#这个是单元格的对齐，不是内容的对其
for i in range(16):
    for j in range(13):
        table.cell(i, j).paragraphs[0].alignment  = WD_PARAGRAPH_ALIGNMENT.CENTER #这里全局设置居中后后面就不用设置了
        table.cell(i, j).vertical_alignment  = WD_CELL_VERTICAL_ALIGNMENT.CENTER


# 添加事项
things_list = ['日期\\项目', '早餐', '口语', '数学', '单词', '午休', '英语', '力扣', '公考', '健身', '钢琴', '阅读', '按时睡觉']
for i in range(13):
    p=table.rows[0].cells[i].paragraphs[0]
    p.text=things_list[i]
    # p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  #单独设置居中的时候可以这样做

#添加备注
bak_list=['8点吃',]

#重构，自动添加参数，打卡模块，自动生成并发送邮件模块模块，自动检测并下载模块


# 生成文件
if os.path.exists('test.docx') is True:
    os.remove('test.docx')
document.save('test.docx')


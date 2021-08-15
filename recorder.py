#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 11:17
# @Author  : hanyou
# @Software: PyCharm
"""
用于实现打卡功能
"""

# 每个事件的前五分钟为打卡时间 or 晚上23点前最后一次打卡显示所有内容，对错过的打卡进行修改并评分
import datetime
from tkinter import *

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

from TimeTableGenerator import get_headline_str
from show_schedule import Clocker

import tkinter
import tkinter.messagebox

from docx import Document


class Recorder:
    def __init__(self):
        # self.__date = datetime.date.today().strftime('%Y%m%d')
        self.__date = '20210816'
        # 创建主窗口
        self.root = tkinter.Tk()
        # 整型对象
        self.var = tkinter.IntVar()

        _, _,self.time_index=Clocker.get_clock_data()

    def get_result(self):

        num = self.var.get()
        # 如果值为1,写入
        # 获取当前单元格位置

        headline_str = get_headline_str(self.__date,record_mode=True)
        f = Document('C:/Users/hy/Desktop/打卡表格/%s.docx' % headline_str)
        table = f.tables[0]
        # 获取哪一天，哪一个项目的id
        # 读取第一列的数字与self.__date比较
        x = None
        for i in range(14):
            if int(table.cell(i + 1, 0).text[-2:]) == int(self.__date[6:8]):
                x = i + 1  # 输出哪一行
        if x == -1:
            ex = Exception("x没有被赋值")
            raise ex
        if self.time_index==0:
            y=12#-1不行
            x=x-1
            if x == 0:#不在这张表格内
                return None#直接中断
        else:
            y = self.time_index-1

        if num == 0:
            table.cell(x, y).paragraphs[0].text = '✔'
            table.cell(x, y).paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            f.save('C:/Users/hy/Desktop/打卡表格/%s.docx' % headline_str)#需要保存！

        else:
            # 暂时不打×
            pass

        # 关闭窗口
        self.root.quit()

    def windows_set(self):
        Time_Dict = ['早餐', '口语', '数学', '单词', '午休', '英语', '力扣', '公考', '健身', '钢琴', '阅读', '按时睡觉']
        if self.time_index-1 >=0:

            text_str=Time_Dict[self.time_index-1]
            print(self.time_index)
        else:
            text_str = Time_Dict[- 1]

        lb = tkinter.Label(self.root, text='%s' % text_str, fg='black', font=("黑体", 50))
        lb.pack()
        # 值为1
        choose_yes = tkinter.Radiobutton(self.root, text="yes", variable=self.var, value=0, font=("cambria", 20))
        choose_yes.pack()
        # 值为2
        choose_no = tkinter.Radiobutton(self.root, text="no", variable=self.var, value=1, font=("cambria", 20))
        choose_no.pack()
        # 按钮
        submit = Button(self.root, text="Submit", command=self.get_result)
        submit.pack()
        self.root.mainloop()

    def statistics_count(self):
        for i in range(14):
            for j in range(12):


    def run_judge(self):
        #某些时段不执行
        if int(self.__date[4:6]) != 2:
            if int(self.__date[6:8]) == 15 or int(self.__date[6:8]) == 30:
                pass  # 不执行
            else:
                self.windows_set()
        else:
            if int(self.__date[6:8]) == 14 or int(self.__date[6:8]) == 28 or int(self.__date[6:8]) == 29:
                pass
            else:
                self.windows_set()

if __name__ == '__main__':
    #线程里面每格时间前五分钟执行，超过五分钟后kill进程
    a=Recorder()
    a.run_judge()
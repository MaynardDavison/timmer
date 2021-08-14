#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 21:36
# @Author  : Maynard Davison
# @Software: PyCharm
"""
生成计时器
"""
import time
from datetime import datetime
import tkinter


def _refresh():
    """
    刷新时间和内容
    Returns: test

    """
    # 获取用于比较的时间表临时列表
    time_list_for_compare = []
    for i in _Time_Dict:
        temp = datetime.strptime(i, "%H:%M:%S")
        time_list_for_compare.append(temp)
    # 获取当前时间
    time_string = datetime.now().strftime("%H:%M:%S")  # 获取当前的时间并转化为字符串

    # 获取用于比较的当前时间
    time_date_type = datetime.strptime(time_string, "%H:%M:%S")

    # 插入用于比较的当前时间进行排序获取id号
    time_list_for_compare.append(time_date_type)
    time_index = sorted(time_list_for_compare).index(time_date_type)

    # 输出时间字符和对应序号，睡觉用None表示
    if time_index == 0 or time_index == len(time_list_for_compare):
        time_index = None
    else:
        time_index = time_index - 1  # -1是因为列表里面加了临时的

    # 显示
    lb.configure(text=time_string)

    if time_index:  # 如果存在
        lb2.configure(text=list(_Time_Dict.values())[time_index])  # 取values的值,需转成list，dict不行
    else:
        lb2.configure(text="睡觉")

    # 设置5s延时
    root.after(5000, _refresh)  # 不能嵌套多个def



# 设置成全局参数，为了after能正常运行
_Time_Dict = {'08:00:00': '早餐', '08:30:00': '口语', '09:00:00': '数学', '11:30:00': '午饭',
              '12:00:00': '单词', '12:30:00': '午觉', '13:30:00': '英语', '16:00:00': '力扣',
              '17:00:00': '公考与国策', '18:00:00': '晚饭', '18:30:00': '休息', '19:00:00': '健身',
              '20:30:00': '洗澡', '21:00:00': '钢琴', '22:00:00': '阅读', '22:30:00': '回复消息',
              '23:00:00': '睡觉'}
# tk 初始化
root = tkinter.Tk()
root.title("时钟")
lb = tkinter.Label(root, text='', fg='black', font=("黑体", 80))
lb2 = tkinter.Label(root, text='', fg='black', font=("黑体", 60))
lb.pack()
lb2.pack()




def creat_window():
    """
    生成函数出口供调用
    Returns: None

    """

    _refresh()
    root.mainloop()

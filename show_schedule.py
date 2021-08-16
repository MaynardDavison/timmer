#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 21:36
# @Author  : Maynard Davison
# @Software: PyCharm
"""
生成计时器
"""
import json
import tkinter


def show_schedule():
    root = tkinter.Tk()
    root.title("时钟")
    lb = tkinter.Label(root, text='', fg='black', font=("黑体", 80))
    lb2 = tkinter.Label(root, text='', fg='black', font=("黑体", 60))
    lb.pack()
    lb2.pack()

    def refresh():
        with open('json_files/d_parameters_sec.json', 'r') as f:
            d_param = json.load(f)
        lb.configure(text=d_param['current_time_str'])  # 时间
        lb2.configure(text=d_param['current_thing_str'])  # 事件

        root.after(5000, refresh)  # 不能有参数传入

    refresh()
    root.mainloop()


if __name__ == '__main__':
    pass
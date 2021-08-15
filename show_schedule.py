#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 21:36
# @Author  : Maynard Davison
# @Software: PyCharm
"""
生成计时器
"""
import tkinter
from d_parameters_sec import d_param

# 必须全局参数的时候可以转成class
class ShowSchedule:
    def __init__(self):
        self.__root = tkinter.Tk()
        self.__root.title("时钟")
        self.__lb = tkinter.Label(self.__root, text='', fg='black', font=("黑体", 80))
        self.__lb2 = tkinter.Label(self.__root, text='', fg='black', font=("黑体", 60))
        self.__lb.pack()
        self.__lb2.pack()

    def _refresh(self):
        self.__lb.configure(text=d_param['current_time_str'])#时间
        self.__lb2.configure(text=d_param['current_thing_str'])#事件
        # 设置5s延时
        self.__root.after(1000, self._refresh)  # 不能有参数传入
        self.__root.mainloop()

    def creat_window(self):
        self._refresh()

if __name__ == '__main__':
    c = ShowSchedule()
    c.creat_window()

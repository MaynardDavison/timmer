#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/8/13 10:35
# @Author  : hanyou
# @Software: PyCharm
import pickle


def creat_pickle():
    _Time_Dict = {'08:00:00': '早餐', '08:30:00': '口语', '09:00:00': '数学',
                  '12:00:00': '单词', '12:30:00': '午觉', '13:30:00': '英语',
                  '16:00:00': '力扣', '17:00:00': '公考', '19:00:00': '健身',
                  '21:00:00': '钢琴', '22:00:00': '阅读', '23:00:00': '睡觉'}
    f = open('_Time_Dict', 'wb')
    pickle.dump(_Time_Dict, f)
    f.close()


def read_pickle():
    f = open('_Time_Dict', 'rb')
    s = pickle.load(f)
    f.close()
    return s

if __name__ == '__main__':
    creat_pickle()

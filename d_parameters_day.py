#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 23:07
# @Author  : hanyou
# @Software: PyCharm
"""
动态参数，天级
"""
import calendar
import datetime

from static_parameters import s_param

d_h_param = dict()
d_h_param['current_date_str'] = datetime.date.today().strftime('%Y%m%d')  # 20210815
d_h_param['year'] = int(d_h_param['current_date_str'][0:4])
d_h_param['month'] = int(d_h_param['current_date_str'][4:6])
d_h_param['day'] = int(d_h_param['current_date_str'][6:8])

d_h_param['days_in_month'] = calendar.monthrange(d_h_param['year'], d_h_param['month'])[1]  # int

# 二月15号也休息，后面空余的画斜杠，每月倒数三天都休息
d_h_param['normal_genTable_day'] = 15
d_h_param['normal_genTable_day'] = d_h_param['days_in_month'] - 3


def headline_str_gen():
    part_str = s_param['cap_number'][int(d_h_param['current_date_str'][0])] + \
               s_param['cap_number'][int(d_h_param['current_date_str'][1])] + \
               s_param['cap_number'][int(d_h_param['current_date_str'][2])] + \
               s_param['cap_number'][int(d_h_param['current_date_str'][3])] + '年' \
               s_param['cap_number'][int(d_h_param['current_date_str'][4])] + \
               s_param['cap_number'][int(d_h_param['current_date_str'][5])]
    if d_h_param['day'] <= d_h_param['normal_genTable_day']:
        return current_headline_str, genTable_headline_str


d_h_param['current_headline_str'], \
d_h_param['genTable_headline_str'] = headline_str_gen()

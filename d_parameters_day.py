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
import json
import os

from static_parameters import s_param

d_h_param = dict()
d_h_param['current_date_str'] = datetime.date.today().strftime('%Y%m%d')  # 20210815
d_h_param['current_date_str_2'] = datetime.date.today().strftime('%Y-%m-%d')
d_h_param['year'] = int(d_h_param['current_date_str'][0:4])
d_h_param['month'] = int(d_h_param['current_date_str'][4:6])
d_h_param['next_month']=d_h_param['month']+1
d_h_param['day'] = int(d_h_param['current_date_str'][6:8])

d_h_param['days_in_month'] = calendar.monthrange(d_h_param['year'], d_h_param['month'])[1]  # int

# 二月15号也休息，后面空余的画斜杠，每月倒数三天都休息
d_h_param['normal_genTable_early_day'] = 15
d_h_param['normal_genTable_later_day'] = d_h_param['days_in_month'] - 3

def headline_str_gen():
    part_str = s_param['cap_number'][int(d_h_param['current_date_str'][0])] + \
               s_param['cap_number'][int(d_h_param['current_date_str'][1])] + \
               s_param['cap_number'][int(d_h_param['current_date_str'][2])] + \
               s_param['cap_number'][int(d_h_param['current_date_str'][3])] + '年' + \
               s_param['cap_number'][int(d_h_param['current_date_str'][4])] + \
               s_param['cap_number'][int(d_h_param['current_date_str'][5])]
    if d_h_param['day'] <= d_h_param['normal_genTable_early_day']:
        current_headline_str = part_str + '月上'
        #再检查一下如果没有文件，也执行生成操作

        if d_h_param['day'] == d_h_param['normal_genTable_early_day']:
            genTable_headline_str = part_str + '月下'
            genTable_mode =s_param['gentable_current_mode_num']
            return current_headline_str, genTable_headline_str ,genTable_mode
        elif not os.path.exists(s_param['file_path'] + '%s' % current_headline_str + s_param['file_tpye']):
            genTable_headline_str = current_headline_str
            genTable_mode= s_param['gentable_repaire_early_mode_num']
            return current_headline_str, genTable_headline_str, genTable_mode
        else:
            return current_headline_str, None ,None
    elif d_h_param['day'] <= d_h_param['normal_genTable_later_day']:
        current_headline_str = part_str + '月下'
        if d_h_param['day'] == d_h_param['normal_genTable_later_day']:
            date_number_str = str(int(d_h_param['current_date_str'][0:6]) + 1)
            genTable_headline_str = s_param['cap_number'][int(date_number_str[0])] + \
                                    s_param['cap_number'][int(date_number_str[1])] + \
                                    s_param['cap_number'][int(date_number_str[2])] + \
                                    s_param['cap_number'][int(date_number_str[3])] + '年' + \
                                    s_param['cap_number'][int(date_number_str[4])] + \
                                    s_param['cap_number'][int(date_number_str[5])] + '月上'
            genTable_mode = s_param['gentable_next_mode_num']
            return current_headline_str, genTable_headline_str ,genTable_mode
        elif not os.path.exists(s_param['file_path'] + '%s' % current_headline_str + s_param['file_tpye']):
            genTable_headline_str = current_headline_str
            genTable_mode = s_param['gentable_repaire_later_mode_num']
            return current_headline_str, genTable_headline_str, genTable_mode
        else:
            return current_headline_str, None,None
    else:
        return None, None,None


d_h_param['current_headline_str'], \
d_h_param['genTable_headline_str'] ,\
d_h_param['genTable_switch']= headline_str_gen()

if d_h_param['day'] == d_h_param['normal_genTable_early_day'] or d_h_param['day'] >= d_h_param[
        'normal_genTable_later_day']:
    d_h_param['rest_day_flag'] = 0 #休息日
else:
    d_h_param['rest_day_flag'] = 1 # 非休息日

with open('json_files/d_parameters_day.json','w') as f:
    json.dump(d_h_param,f)


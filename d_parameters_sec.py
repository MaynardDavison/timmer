#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 18:11
# @Author  : hanyou
# @Software: PyCharm
import datetime
import json
import time

# from param_generator import d_param_gen
from static_parameters import s_param

"""
动态参数,秒级
"""
d_param = dict()

d_param['current_time_str'] = datetime.datetime.now().strftime("%H:%M:%S")  # 17:55:10


def d_param_gen():
    """

    Returns:
        生成当前事件的索引，名称；上一项事件的索引，名称

    """
    schedule_thing_list = s_param['schedule_thing_list']
    schedule_time_list = s_param['schedule_time_list']
    current_time_str = d_param['current_time_str']
    schedule_time_list.append(current_time_str)  # append没返回值
    schedule_time_list_for_compare = schedule_time_list
    current_time_index_for_compare = sorted(schedule_time_list_for_compare).index(current_time_str)
    schedule_time_list_for_compare_len = len(schedule_time_list_for_compare)
    if current_time_index_for_compare == 0 or current_time_index_for_compare == schedule_time_list_for_compare_len:
        current_time_index = s_param['things_len']  # 最后一个
    else:
        current_time_index = current_time_index_for_compare - 1
    current_thing_str = schedule_thing_list[current_time_index]
    if current_time_index == 0:
        last_time_index = s_param['things_len']  # 最后一个
    else:
        last_time_index = current_time_index - 1
    last_thing_str = schedule_thing_list[last_time_index]
    return current_time_index, current_thing_str, last_time_index, last_thing_str


d_param['current_time_index'], \
d_param['current_thing_str'], \
d_param['last_time_index'], \
d_param['last_thing_str'] = d_param_gen()

d_param['current_thing_time']=s_param['schedule_time_list'][d_param['current_time_index']]

# d_param['current_thing_time_for compare'] =datetime.datetime.strptime(d_param['current_thing_time'], "%H:%M:%S")
# d_param['current_time_str_for_compare'] = datetime.datetime.strptime(d_param['current_time_str'], "%H:%M:%S")


# 参数封闭，需要中间文件传递参数
with open('json_files/d_parameters_sec.json','w') as f:
    json.dump(d_param,f)

# if __name__ == '__main__':
#     a=datetime.datetime.strptime(d_param['current_time_str'], "%H:%M:%S")-\
#     datetime.datetime.strptime(d_param['current_thing_time'], "%H:%M:%S")
    # a= d_param['current_time_str']-d_param['current_thing_time']


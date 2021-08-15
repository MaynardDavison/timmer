#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 0:45
# @Author  : hanyou
# @Software: PyCharm
from d_parameters_day import d_h_param
from static_parameters import s_param

part_str = s_param['cap_number'][int(d_h_param['current_date_str'][0])] + \
               s_param['cap_number'][int(d_h_param['current_date_str'][1])] + \
               s_param['cap_number'][int(d_h_param['current_date_str'][2])] + \
               s_param['cap_number'][int(d_h_param['current_date_str'][3])] + '年' \
               s_param['cap_number'][int(d_h_param['current_date_str'][4])] + \
               s_param['cap_number'][int(d_h_param['current_date_str'][5])]
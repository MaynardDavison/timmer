#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 17:49
# @Author  : hanyou
# @Software: PyCharm

# 其他月份
"""
静态参数
"""

s_param = dict()

s_param['schedule_dict'] = {'08:00:00': '早餐', '08:30:00': '口语', '09:00:00': '数学',
                            '12:00:00': '单词', '12:30:00': '午觉', '13:30:00': '英语',
                            '16:00:00': '力扣', '17:00:00': '公考', '19:00:00': '健身',
                            '21:00:00': '钢琴', '22:00:00': '阅读', '23:00:00': '睡觉'}

s_param['schedule_thing_list'] = ['早餐', '口语', '数学', '单词', '午休', '英语', '力扣', '公考', '健身', '钢琴', '阅读', '按时睡觉']
s_param['schedule_time_list'] = [x for x in s_param['schedule_dict']]#['08:00:00', '08:30:00', '09:00:00',...]

s_param['things_len'] = len(s_param['schedule_dict'])  # 12
s_param['days_len'] = 14  # 一个表格记14天

# 表格参数
s_param['table_col_len'] = s_param['things_len'] + 1  # 13
s_param['table_row_len'] = s_param['days_len'] + 2  # 16

s_param['table_col_list']=['日期\\项目', '早餐', '口语', '数学', '单词', '午休', '英语', '力扣', '公考', '健身', '钢琴', '阅读', '按时睡觉']
s_param['bak_list']=['备注', '8点', '流利说', '考研数学', '', '', 'anki复习', 'c&python', '党，写作，刷题', '两天一轮', '', 'caculus', '23:00']
s_param['col_width_list']=[2.13, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 1.92, 2.13]


s_param['cap_number']=['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
s_param['file_path']= 'C:/Users/hy/Desktop/打卡表格/'
s_param['file_tpye']='.docx'



s_param['genTable_next_month_start_day']=1
s_param['genTable_current_month_start_day']=16

s_param['gentable_current_mode_num']=0
s_param['gentable_next_mode_num']=1
s_param['gentable_repaire_early_mode_num']=2
s_param['gentable_repaire_later_mode_num']=3

s_param['task_complete_value'] = 0
s_param['task_not_complete_value'] = 1
# s_param['pop_interval_time']=300
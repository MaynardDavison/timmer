#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 0:45
# @Author  : hanyou
# @Software: PyCharm
import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from d_parameters_day import d_h_param
from static_parameters import s_param

a=15
b=28
c=15
def test():
    print(a)
def test2():
    print(b)
    # schedudler.remove_all_jobs()
#     schedudler.shutdown(wait=False)
# run_date='2021-8-16 20:24:30'
# run_date2='2021-8-16 20:25:00'
# schedudler = BlockingScheduler()
# schedudler.add_job(test, 'date', run_date=run_date)
# schedudler.add_job(test2, 'date', run_date=run_date2)
# schedudler.start()

print(datetime.date.today().strftime('%Y-%m-%d')+' '+'1')

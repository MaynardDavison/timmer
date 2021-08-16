#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 21:36
# @Author  : hanyou
# @Software: PyCharm
import os

from recorder import record_trigger
from show_schedule import *
import threading
from apscheduler.schedulers.blocking import BlockingScheduler
from multiprocessing import Process, Pool




def run_show():
    with open('json_files/d_parameters_day.json', 'r') as f:
        d_h_param = json.load(f)
    if d_h_param['rest_day_flag']==1:
        show_schedule()
def run_record():
    with open('json_files/d_parameters_day.json', 'r') as f:
        d_h_param = json.load(f)
    if d_h_param['rest_day_flag']==1:
        record_trigger()

def update_sec():
    thread_lock.acquire()
    os.system('python d_parameters_sec.py')
    thread_lock.release()
    print('update_sec')


def update_day():
    thread_lock.acquire()
    os.system('python d_parameters_day.py')
    thread_lock.release()
    print('update_day')



def run_update():
    #首先定时执行 更新sec day操作
    update_sec()#启动时先执行一次
    update_day()
    schedudler = BlockingScheduler()
    schedudler.add_job(update_sec, 'interval',seconds=5)
    schedudler.add_job(update_day,'cron', day_of_week='*', hour=7, minute='50', second='00') #每天执行一次

    schedudler.start()
    # t1 = threading.Thread(target=judge_date_to_run, name='show')
    # t1.start()


if __name__ == '__main__':
    thread_lock = threading.Lock()
    pool = Pool(processes=3)
    pool.apply_async(run_update)
    pool.apply_async(run_show)
    pool.apply_async(run_record)
    pool.close()
    pool.join()
    #
    # # 一个读一个写没问题，但是容易间隔不均匀
    # # t1 =threading.Timer(5,update)#只是延时执行
    # t1 = threading.Thread(target=update, name='update_param')
    # t1.start()
    #
    # t2 = threading.Thread(target=judge_date_to_run, name='show')
    # t2.start()
    #
    # with open('json_files/d_parameters_day.json', 'r') as f:
    #     d_h_param = json.load(f)
    # if d_h_param['rest_day_flag'] == 1:
    #     record_trigger()
    #
    #
    # #设置成定时执行即可
    # os.system('python d_parameters_day.py')
    # with open('json_files/d_parameters_day.json', 'r') as f:
    #     d_h_param = json.load(f)
    # if d_h_param['genTable_switch']:
    #     static_score()
    #     creat_table()




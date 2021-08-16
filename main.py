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
    # thread_lock.acquire()
    os.system('python d_parameters_sec.py')
    # thread_lock.release()



def update_day():
    # thread_lock.acquire()
    os.system('python d_parameters_day.py')
    # thread_lock.release()




def run_update():
    #首先定时执行 更新sec day操作
    update_sec()#启动时先执行一次
    update_day()
    schedudler = BlockingScheduler()
    schedudler.add_job(update_sec, 'interval',seconds=5)
    schedudler.add_job(update_day,'cron', day_of_week='*', hour=7, minute='50', second='00') #每天执行一次
    schedudler.start()
    # t = threading.Thread(target=judge_date_to_run, name='show')
    # t.start()


if __name__ == '__main__':
    # thread_lock = threading.Lock() #进程锁为什么不行？schedule的原因？
    # run_update()
    # pool = Pool(processes=3)
    # pool.apply_async(run_update)
    # pool.apply_async(run_show)
    # pool.apply_async(run_record)
    # pool.close()
    # pool.join()
    #为什么这样可以而进程池不行？
    p = Process(target=run_update)
    p.start()
    p = Process(target=run_show)
    p.start()
    p = Process(target=run_record)
    p.start()
    p.join()





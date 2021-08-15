#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 21:36
# @Author  : hanyou
# @Software: PyCharm
import os
import time

from show_schedule import *
import threading
from TimeTableGenerator import timed_generation
from apscheduler.schedulers.blocking import BlockingScheduler
from multiprocessing import Process, Pool
from show_schedule import ShowSchedule
from d_parameters_sec import update_d_param_process


def thread2():
    # 定时任务
    schedudler = BlockingScheduler()
    # 定时每天 20:00:00秒执行任务
    schedudler.add_job(timed_generation, 'cron', day_of_week='0-6', hour=20, minute=00, second=00)  # cron应该时触发器的名称
    print('test')
    schedudler.start()  # 开始任务

def thread3():
    s = read_pickle()
    schedudler = BlockingScheduler()
    for key, value in s.items():
        schedudler.add_job(timed_generation, 'cron', day_of_week='0-6', hour=int(key[0:2]), minute=int(key[3:5]), second=00)



def update():
    while True:
        os.system('python d_parameters_sec.py')
        time.sleep(1)

# t = threading.Thread(target=creat_window, name='thread1')#多线程


if __name__ == '__main__':
    # 多进程
    pool = Pool(processes=3)
    pool.apply_async(update_d_param_process())
    pool.apply_async(ShowSchedule.creat_window)
    pool.apply_async(thread2)
    pool.close()
    pool.join()

# 线程1，时钟
# 线程2，打卡弹窗
# 线程3，生成表格

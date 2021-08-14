#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 21:36
# @Author  : hanyou
# @Software: PyCharm
import time


from clock import *
import threading
from TimeTableGenerator import timed_generation
from apscheduler.schedulers.blocking import BlockingScheduler
from multiprocessing import Process, Pool



# 重构，自动添加参数，打卡模块，自动生成并发送邮件模块模块，自动检测并下载模块

# 设置一个线程时间日期到了自动生成表格，还不能重复

# 打卡设计

# 消息发送，’新周报已生成+之前打卡情况‘

# 未来考试后再改进自适应的列数目和项目


# creat_window()


def thread2():
    # 定时任务
    schedudler = BlockingScheduler()
    # 定时每天 20:00:00秒执行任务
    schedudler.add_job(timed_generation, 'cron', day_of_week='0-6', hour=20, minute=00, second=00)  # cron应该时触发器的名称
    print('test')
    schedudler.start()  # 开始任务


# t = threading.Thread(target=creat_window, name='thread1')#多线程




if __name__ == '__main__':

    # 多进程
    pool = Pool(processes=2)
    pool.apply_async(creat_window)
    pool.apply_async(thread2)
    pool.close()
    pool.join()


# 线程1，时钟
# 线程2，打卡弹窗
# 线程3，生成表格


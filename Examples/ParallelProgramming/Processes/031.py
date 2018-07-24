#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
进程池 Pool
'''

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    if name == 1: # 即使进程 1 挂掉了，其他进程还可以继续执行
        l = [1, 2, 3, 4]
        s = l[5]
        print(s)
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4) # 进程池
    for i in range(5): # 跑 5 个任务
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
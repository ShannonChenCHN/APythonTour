#!/usr/bin/python
# -*- coding: utf-8 -*-

''''
多进程
'''

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join() # 等待子进程结束后再继续往下运行
    print('Child process end.')
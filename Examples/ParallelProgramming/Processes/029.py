#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
多进程
'''


import os

'''创建子进程'''
print('Process (%s) start...' % os.getpid())

pid = os.fork() # 父进程返回子进程的 id，子进程永远返回 0
if pid == 0:
    # 子进程通过 getpid() 拿到自己的进程 id，getppid()拿到父进程的 id
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

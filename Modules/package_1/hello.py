#!/usr/bin/python
# -*- coding: utf-8 -*-


"""a test module"""

__author__ = 'Shannon Chen'


import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__=='__main__':
    test()


#================= 访问限制 ===================

def _private_func_1(name):
    return 'Hello, %s' % name


def _private_func_2(name):
    return 'Hey, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_func_1(name)
    else:
        return _private_func_2(name)

print(greeting('Shannon'))
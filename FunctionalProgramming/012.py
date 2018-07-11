#!/usr/bin/python
# -*- coding: utf-8 -*-

# 闭包


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

# 输出 9 9 9
print(f1(), f2(), f3())


def func():
    def makeFunc(i):
        def f():
            return i * i
        return f

    fs = []
    for i in range(1, 4):
        fs.append(makeFunc(i))
    return fs

f4, f5, f6 = func()

# 输出 1 4 9
print(f4(), f5(), f6())
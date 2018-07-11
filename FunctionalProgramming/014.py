#!/usr/bin/python
# -*- coding: utf-8 -*-


print(int('10'))
print(int('10', base=2))


def int2(x, base=2):
    return int(x, base)
print(int2('10'))


## 偏函数
import functools

partailInt2 = functools.partial(int, base=2)
print(partailInt2('10'))



def myFunc(a, b=2):
    print(a, b)
myFunc(2)

myFuncNew = functools.partial(myFunc, b=4) # 这里 4 作为默认参数
myFuncNew(2)

myFuncNew_1 = functools.partial(myFunc, 3) # 这里 3 作为必需参数
myFuncNew_1(2)


maxNew = functools.partial(max, 10)# 这里 10 作为必需参数
print(maxNew(2, 6, 9))
#!/usr/bin/python
# -*- coding: utf-8 -*-


# 列表生成式

L1 = list(range(1, 11))
print(L1)

L2 = [x * x for x in range(1, 11)]
print(L2)

## 筛选条件
L3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L3)

## 双循环
L4 = [m + n for m in 'ABC' for n in 'XYZ']
print(L4)

## 使用两个变量来生成 list
d = {'baidu': 'www.baidu.com', 'tencent': 'www.qq.com', 'amazon': 'www.amazon.com'}
[k + '=' + v for k, v in d.items()]
print(d)

L5 = ['Hello', 'World', 'IBM', 'Apple']
L5_lower = [s.lower() for s in L5]
print(L5_lower)


# 打印当前目录下的所有文件名
import os
ls = [d for d in os.listdir('.')]
print(ls)


#!/usr/bin/python
# -*- coding: utf-8 -*-


# 迭代

## 字典
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, ':',  d[key])

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, ':', value)

print('=================')

## 字符串

for c in 'English':
    print(c)



print('=================')
## 数组

for num in [2, 56, 23]:
    print(num)

for i, value in enumerate([3, 56, 23]):
    print(i, value)


for x, y in [(1, 1), (2, 3), (5, 8)]:
    print(x, y)

print('=================')

## 判断一个对象是不是可迭代对象

from collections.abc import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))
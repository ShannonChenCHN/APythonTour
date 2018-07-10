#!/usr/bin/python
# -*- coding: utf-8 -*-


# 生成器

## 方式一
g = (x * x for x in range(10))
print(g)


print(g.__next__())
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for n in g:
    print(n)


# 使用生成器实现一个斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for i in fib(6):
    print(i)


print('===================')

# 迭代器

## 可迭代对象
from collections.abc import Iterable

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(10, Iterable))


## 迭代器
from collections.abc import Iterator

print(isinstance((x for x in  range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

## 通过 iter() 函数可以把 list、dict、str 变成 Iterator
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
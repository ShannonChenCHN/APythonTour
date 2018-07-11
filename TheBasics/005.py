#!/usr/bin/python
# -*- coding: utf-8 -*-

# 函数

## 调用函数
a = abs(100)

b = abs(-100)

print(a, b)


print(max(34, 12, 55))


## 数据类型转换
print(int('123'), int(12.34), float('12.34'), str(1.23), bool(1))

aFunction = abs # 变量 aFunction 指向函数对象 abs
print(aFunction(-2.34))

## 定义函数
def custom_abs(x):
    if not isinstance(x, (int, float)):    # 参数类型检查
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return
print(custom_abs(-34))
# print(custom_abs('dd'))

### 函数可以嵌套定义
def func(x, y):
    def square(x):
        return x * x
    return square(x) + y

print('嵌套函数：', func(3, 4))


### 空函数
def nop():
    pas

### 返回值为 Tuple

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

targetPoint = move(100, 100, 60, math.pi / 6)
print(targetPoint)



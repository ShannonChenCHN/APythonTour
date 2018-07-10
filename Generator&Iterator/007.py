#!/usr/bin/python
# -*- coding: utf-8 -*-

# 切片（slice）

## 数组
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] ==> ', L[0:3])  # 取出前 n 个元素
print('L[:3] ==> ', L[:3])

print('L[1:3] ==> ', L[1:3])
print('L[-3:]  ==> ', L[-3:])
print('L[-3:-1] ==> ', L[-3:-1])
print('L[:] ==> ', L[:])
print('L[::2] ==> ', L[::2])


## tuple
T = (0, 1, 2, 3, 4, 5)
print('T[:3]  ==> ', T[:3])

## string
S = 'ABCDEFG'
print('S[:2] ==> ', S[:2])
print('S[::2] ==> ', S[::2])
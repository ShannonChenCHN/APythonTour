#!/usr/bin/python
# -*- coding: utf-8 -*-

# 高阶函数


# map 函数
# map 函数接受两个参数：一个是函数，一个是 iterable；
# map 函数将传入的函数依次作用到序列的每个元素上，并把结果作为 Iterator 返回

def square(x):
    return x * x

result = map(square, [1, 2, 3, 4, 5, 6, 7])
print(list(result))


strList = list(map(str, [1, 2, 3, 4, 5, 6, 7]))
print(strList)


# reduce 函数
# reduce 函数必须接受两个参数：一个是函数，一个是序列 sequence
# reduce 函数把接受的函数首先应用到序列的最前面的两个元素上，然后再把结果和序列的下一个元素做累计计算，
# 以此类推，最后返回最终的累加结果
from functools import reduce
def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))


# filter 函数
# filter 函数接受两个参数：一个是函数，另一个是序列。
# filter 函数把传入的函数依次作用于每个元素，然后根据参数函数返回的结果是 True 还是 False 决定保留还是丢弃该元素
# filter 函数数返回的是一个 Iterator，也就是一个惰性序列。因此如果要直接拿到最终结果，需要用 list() 函数将结果转为 list
# 一句话概括，filter 函数的作用如同其名，就是用来筛选出符合条件的。

def is_odd(n):
    return n % 2 == 1
oddArray = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print('奇数：', oddArray)


# sorted 函数
print(sorted([36, 5, -12, 9, -21]))

print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))





####################################################################################

# 练习
## 1. 字符串转成数字：现将字符串转成数字数组，然后再转成一个数字
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2nums(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2nums, s))

print(str2int('3456677'))


def normalize(name):
    result = ''
    for i, c in enumerate(name):
        if i == 0:
            result += c.upper()
        else:
            result += c.lower()

    return result



print(list(map(normalize, ['adam', 'LISA', 'barT'])))


## 2. 接受一个 list， 使用 reduce 求积

def prod(L):
    def multiply(x, y):
        return x * y
    return reduce(multiply, L)

print(prod([3, 4, 5]))


# 3. 用 filter 求素数

# 原理(埃氏筛法)：https://baike.baidu.com/item/%E5%9F%83%E6%8B%89%E6%89%98%E8%89%B2%E5%B0%BC%E7%AD%9B%E9%80%89%E6%B3%95
# （1）先把1删除（现今数学界1既不是质数也不是合数）
# （2）读取队列中当前最小的数2，然后把2的倍数删去
# （3）读取队列中当前最小的数3，然后把3的倍数删去
# （4）读取队列中当前最小的数5，然后把5的倍数删去
# （5）读取队列中当前最小的数7，然后把7的倍数删去
# （6）如上所述直到需求的范围内所有的数均删除或读取

# 实现起来主要需要两个部分：
# 一个生成器用于保存奇数的序列
# 一个判断是否是素数的函数

def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _is_not_divisible(n):
    return lambda x: x % n != 0

def primes():
    yield 2
    iterator = _odd_iter()  # 最初拿到从 2 开始的序列
    while True:
        n = next(iterator)  # 拿出序列中第一个数字
        yield n
        iterator = filter(_is_not_divisible(n), iterator)  # 筛选出不能被 n 整除的数


# 打印 1000 以内的素数
for n in primes():
    if n < 100:
        print(n)
    else:
        break

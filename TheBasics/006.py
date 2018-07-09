#!/bin/python
# -*- coding: utf-8 -*-

# 默认参数
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Lindsey', 'F')
enroll('Tom', 'M', 7) # 按顺序提供默认参数
enroll('Adam', 'M', city='Shanghai') # 不按顺序提供参数


# 可变参数

## 使用 list 或者 tuple 作为参数
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# print(calc([1, 2, 3]))


## 可变参数
def calc(*numbers):
    print(numbers)
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
numbers = [1, 2, 3]
print(calc(numbers[0], numbers[1], numbers[2]))
print(calc(*numbers))
print(calc(1, 2))


## 关键字参数
def person(name, age, **kw):
    if 'city' in kw: #检查是否有 city 参数
        pass
    if 'job' in kw:
        pass
    print('name: ', name, 'age: ', age, 'other: ', kw)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Shannon', 25, **extra)
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 命名关键字参数
def student(name, age, *, city='Beijing', sex):
    print('name: ', name, 'age: ', age, 'sex: ', sex, 'city: ', city)

student('Tim', 24, sex='M')
# student('Mark', 24) # 只有有默认值的参数才可以缺省
# student('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456) # 不允许有多余的参数


def teacher(name, age, *args, city):
    print('name: ', name, 'age: ', age, 'city: ', city, 'other', args)

teacher('Paul', 34, 'optionalArg', city='Beijing')
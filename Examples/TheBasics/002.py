#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# list

classmates = ['Michael', 'Bob', 'Tracy']

print(classmates)
print(len(classmates))

print(classmates[0])
print(classmates[-1])

classmates.append('Adam')
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)

classmates[1] = 'Sarah'
print(classmates)

n = ['Jane', 'Mac', 'Jason']

print(classmates + n)


# Tuple

# Tuple 与 list 类似，但是不可变
t1 = (1, 2)
t2 = ()
t3 = (1,)

print(t1)
print(t2)
print(t3)
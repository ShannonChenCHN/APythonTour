#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-


age = 20

if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('your age is', age)
    print('teenager')
else:
    print('kid')


birthStr = input('birth: ')
birth = int(birthStr)
if birth < 2000:
    print('00前')
else:
    print('00后')
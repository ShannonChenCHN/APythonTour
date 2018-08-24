#!/usr/bin/python
# -*- coding: utf-8 -*-

import types

class Animal(object):
    def __init__(self, name='Animal'):
        self.name = name

    def run(self):
        print('Animal is running...')


class Dog(Animal):
    pass

def func():
    pass

## type() 函数
print(type(123), type(123) == int)
print(type(Animal()))
print(type(func), type(func) == types.FunctionType)
print(type(abs), type(abs) == types.BuiltinFunctionType)

print(type(None))

lambdaType = lambda x : x + 1
print(type(lambdaType), type(lambdaType) == types.LambdaType)

gneratorType = (x for x in range(10))
print(type(gneratorType), type(gneratorType) == types.GeneratorType)


## isinstance() 函数

print(isinstance(Dog(), Animal))
print(isinstance(Dog(), Dog))
print(isinstance([1, 2], (list, tuple)))



## dir() 函数

pig = Animal('pig')
print(dir(pig))
print(hasattr(pig, 'name'))
setattr(pig, 'name', 'pig')
print(getattr(pig, 'name'))
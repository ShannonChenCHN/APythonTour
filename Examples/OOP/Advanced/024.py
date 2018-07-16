#!/usr/bin/python
# -*- coding: utf-8 -*-


# 1. 使用type()函数动态创建类

from myclass import MyClass

myObj = MyClass()
print(type(MyClass), type(myObj))



## type()函数既可以返回一个对象的类型，又可以创建出新的类型
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()
print(type(Hello), type(h))



# 2. 元类
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value) # 添加一个 add 方法
        print('cls: ', cls, ',')
        print('name:', name, ',')
        print('bases: ', bases, ',')
        print('attrs:', attrs)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add('a')
print(L)
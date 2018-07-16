#!/usr/bin/python
# -*- coding: utf-8 -*-


# 面向对象

class Student(object):

    # 在 init 方法中绑定属性
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


paul = Student('Paul', 98)
print(Student)
print(paul)
paul.print_score()
# print(paul.__name)
print(paul.get_name())
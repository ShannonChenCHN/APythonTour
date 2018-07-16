#!/usr/bin/python
# -*- coding: utf-8 -*-


# __slots__ 的使用


class Student(object):
    __slots__ = ('name', 'age', 'set_age', 'score')
    pass

# 创建一个实例对象
s = Student()

# 动态给实例绑定一个属性
s.name = 'Michael'
print(s.name)    # Michael

# 定义一个函数作为实例方法
def set_age(self, age):
     self.age = age
     print(self, age)

# 给实例绑定一个方法
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(26) # 调用实例方法

# 如果不将函数转成 MethodType 类型的话，这个方法内部的 self 就需要显式传入了
# s.set_age = set_age
# s.set_age(s, 26)


print(s.age)
print(dir(s))

def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(100)
print(s.score)  # 输出 100


# s.sex = 'M' # __slot__ 中没有声明 sex 属性，所以会报错

class HighSchoolStu(Student):
    pass

hs = HighSchoolStu()
hs.sex = 'M'  # __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的


class GraduateStudent(Student):
    __slots__ = ('sex') # 如果子类中也定义了 __slots__，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
    pass

g = GraduateStudent()
g.sex = 'F'
g.score = 100
# g.city = 'Shanghai'  # 父类和子类的 __slot__ 中均没有声明 city 属性，所以会报错
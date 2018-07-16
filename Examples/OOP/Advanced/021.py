#!/usr/bin/python
# -*- coding: utf-8 -*-



# 多继承

class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

# 各种动物:
class Dog(Mammal, RunnableMixIn):
    pass

class Bat(Mammal, FlyableMixIn):
    pass

class Parrot(Bird, FlyableMixIn):
    pass

class Ostrich(Bird, FlyableMixIn):
    pass

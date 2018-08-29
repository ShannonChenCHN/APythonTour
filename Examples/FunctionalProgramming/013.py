#!/usr/bin/python
# -*- coding: utf-8 -*-

"""装饰器"""

import functools


# ===============================
#           最基本的decorator
# ===============================

def log(func):
    @functools.wraps(func)  # 把原始函数的__name__等属性复制到 wrapper()函数中
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2018-3-25')

# 上面的 @log 相当于 now = log(now)

now()
print(now.__name__)

print('=' * 50)

# ===============================
#           三层嵌套的decorator
# ===============================

def log_1(text):

    def decorator(func):
        @functools.wraps(func) # 把原始函数的__name__等属性复制到 wrapper()函数中
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log_1('execute')
def today():
    print('2018-3-25')

today()

print(today.__name__)



# ===============================
#           类 decorator
# ===============================

class Foo(object):

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('class decorator satrt running')
        self._func()
        print('class decorator ending')


@Foo
def bar():
    print('bar')

bar()
# print(bar.__name__)

# 上面的代码相当于
# def bar():
#     print('bar')
# obj = Foo(bar)
# obj.__call__()
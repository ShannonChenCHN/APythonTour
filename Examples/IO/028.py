#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
序列化
'''


import pickle, os

# 序列化
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

# 写入文件
filepath = 'dump.txt'
f = open(filepath, 'wb')
pickle.dump(d, f)
f.close()

# 读取文件，反序列化
readfile = open(filepath, 'rb')
d = pickle.load(readfile)
print(d)
readfile.close()

os.remove(filepath)



'''
JSON
'''

import json

# 序列化
print(json.dumps(d))

# 反序列化
json_str = '{"name": "Bob", "age": 20, "score": 88}'
result_dict = json.loads(json_str)
print(result_dict)


# class 的序列化和反序列化
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 21, 89)
print(json.dumps(s, default=lambda obj: obj.__dict__))


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
print(json.loads(json_str, object_hook=dict2student))
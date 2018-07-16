#!/usr/bin/python
# -*- coding: utf-8 -*-


# 文件读写


try:
    f = open('../../LICENSE', 'r')
    print(f.read(100))
    # print(f.readlines())
    # print(f.read())
    f.close()

finally:
    if f:
        f.close()


with open('../../LICENSE', 'r', encoding='utf-8') as f:
    print(f.read())

with open('../../python_logo.png', 'rb') as img:
    print(img.read())



with open('./test.txt', 'w') as fileToWrite:
    fileToWrite.write('Hello, world!')

with open('./test.txt', 'w') as fileToWrite:
    fileToWrite.write('Hello, world!')
#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

# 输入和输出
name = input('Please enter your name: ')
print('hello', name)


# 数据类型、变量
a = 6
b = 12
print(a + b)

if a > 0 and b > 0:
    print('a and b both are greater than 0.')

c = True
if c == True:
    print("c is True")
else: 
    print('c is not True')


d = None
print(d)

# 所谓的"常量"
PI = 3.14159265359
print(PI)

# 运算
print(10 / 3)
print(10 // 3)
print(10 % 3)


# 字符串
string = '中文'
encodedString = string.encode('utf-8')
print(encodedString)
print(encodedString.decode('utf-8'))

print(len(string))
x = b'ABC'
x_1 = 'ABC'.encode('utf-8')
x_2 = 'ABC'.encode('ascii')
y = 'ABC'
z = u'ABC'
print(x, x.decode('utf-8'), y, z)
print(len('中文'), len('中文'.encode('utf-8')))

# 格式化
print('hello, %s, you have $%d.' % ('Michael', 100000))
print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format("小明", 17.125))
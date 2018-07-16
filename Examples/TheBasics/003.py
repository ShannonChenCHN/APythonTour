#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-



# if-else

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

# for 循环

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

numsFrom0To5 = list(range(0, 6))
sum = 0
for num in numsFrom0To5:
    print(num)
    sum += num

print(sum)


# while 循环
sum = 0
while sum < 100:
    if sum < 50:
        print('sum is less than 50')

    if sum > 70:
        break

    print(sum)
    sum += 10

print(sum)
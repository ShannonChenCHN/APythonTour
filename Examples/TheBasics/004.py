#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-



# dict

ageOfPeople = {"Paul": 17, "Chris": 23, "Mark": 36}
print(ageOfPeople)

ageOfPeople["Chris"] = 24
print(ageOfPeople)

print('Thomas' in ageOfPeople)
print(ageOfPeople.get('Thomas', -1))

ageOfPeople.pop('Paul')
print(ageOfPeople)

# print(ageOfPeople['John']) # 会报错
print(ageOfPeople.get('John'))

# set

setA = set([1, 2, 3])
print(setA)


setB = set([1, 3])
print(setB)


setB.add(5)
setB.remove(1)
print(setB)


setC = setA & setB
print(setC)


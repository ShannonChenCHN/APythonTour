#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
协程
'''

def consumer():
    r = ''
    while True:
        n = yield r # 3. n = 1 ;  5. r = '200 OK' 8. n = 2;  10. r = '200 OK'
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n) # 4. Consuming 1  9. Consuming 2
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1  # 1. n=1 ; 7. n=2
        print('[PRODUCER] Producing %s...' % n)    # 2. Producing 1, 2
        r = c.send(n)  # send(1)   send(2)
        print('[PRODUCER] Consumer return: %s' % r)  # 6. Consumer return: 200 OK
    c.close()

c = consumer()
produce(c)
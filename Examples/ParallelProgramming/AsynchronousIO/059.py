#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
async/await
'''


import threading
import asyncio

async def hello_A():
    print('Hello world A! (%s)' % threading.currentThread())
    await asyncio.sleep(6)
    print('Hello again A! (%s)' % threading.currentThread())

async def hello_B():
    print('Hello world B! (%s)' % threading.currentThread())
    await asyncio.sleep(4)
    print('Hello again B! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello_A(), hello_B()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

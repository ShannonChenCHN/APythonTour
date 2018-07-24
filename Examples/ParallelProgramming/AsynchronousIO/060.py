#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
asyncio 的使用
https://demos.aiohttp.org/en/latest/tutorial.html
'''

import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body='<h1>Index</h1>'.encode('utf-8'), content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')


app = web.Application()
app.add_routes([web.get('/', index),
                web.get('/hello/{name}', hello)])
web.run_app(app)
print('Server started at http://127.0.0.1:8080...')
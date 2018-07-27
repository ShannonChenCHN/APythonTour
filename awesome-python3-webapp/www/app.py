

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time

from datetime import datetime

from aiohttp import web



def index(request):
    return web.Response(body='<h1>This My 1st web project<h1>'.encode('utf-8'), content_type='text/html')


def initApp():
    app = web.Application()
    app.add_routes([web.get('/', index)])
    web.run_app(app)


initApp()
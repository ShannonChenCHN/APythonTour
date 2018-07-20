#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
web 应用
'''

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['USER'] or 'web')
    print(environ)
    return [body.encode('utf-8')]
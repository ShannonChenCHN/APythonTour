#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
网络编程 - TCP 请求 - 服务端

功能：接受客户端请求带过来的字符串，加上 hello 后返回给客户端
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接:
s.connect(('127.0.0.1', 9999))


# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
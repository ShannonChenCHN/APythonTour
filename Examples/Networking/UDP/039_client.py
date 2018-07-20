#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
网络编程 - UDP 请求 - 客户端

功能：接受客户端请求带过来的字符串，加上 hello 后返回给客户端
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))

    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

# 关闭连接
s.close()
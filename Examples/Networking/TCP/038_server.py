#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
网络编程 - TCP 请求 - 服务端

功能：接受客户端请求带过来的字符串，加上 hello 后返回给客户端
'''

import socket, threading, time

# 创建 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 监听客户端 ip 和端口:
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()

    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


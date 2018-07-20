#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
数据库 - SQLite
'''

import sqlite3, os

database = 'test.db'

def writeDataToDB(id, name):

    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect(database)

    # 创建一个Cursor:
    cursor = conn.cursor()

    # 执行一条SQL语句，创建user表:
    tablename = 'user'
    cursor.execute('create table if not exists %s (id varchar(20) primary key, name varchar(20))' % (tablename, ))

    # 继续执行一条SQL语句，插入一条记录:
    cursor.execute('insert into user (id, name) values (?, ?)', (id, name))

    # 通过rowcount获得插入的行数:
    print('row count', cursor.rowcount)

    # 关闭Cursor:
    cursor.close()

    # 提交事务:
    conn.commit()

    # 关闭Connection:
    conn.close()

def readDataFromDB():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # 执行查询语句:
    cursor.execute('select * from user where id=?', ('1',))

    # 获得查询结果集:
    values = cursor.fetchall()

    cursor.close()

    return values


writeDataToDB(1, 'Shannon')
print(readDataFromDB())
os.remove(database)
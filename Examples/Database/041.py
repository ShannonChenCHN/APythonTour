#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
数据库 - MySQL
'''


'''
直接运行会报错：mysql.connector.errors.ProgrammingError: 1049 (42000): Unknown database 'test'

解决方法：
1.打开 mysql 5.7 command line client     # 这是一个mysql自己的命令行
2.输入 show databases;                   # 查看数据库，不要忘记';'，否则无法通过
3.输入 create database test;             # 创建'test'这个数据库

https://www.liaoxuefeng.com/discuss/001409195742008d822b26cf3de46aea14f2b7378a1ba91000/001472552131291bb9dda3a0cfb45d0a510ede18b4bf98f000?page=1

'''


import mysql.connector

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
database = 'test'
conn = mysql.connector.connect(user='root', password='123456', database=database, unix_socket="/tmp/mysql.sock", port='0')


'''插入数据'''

# 创建一个Cursor:
cursor = conn.cursor()

# 执行一条SQL语句，创建user表:
tablename = 'user'
cursor.execute('create table if not exists %s (id varchar(20) primary key, name varchar(20))' % (tablename, ))


# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Shannon'])

# 通过rowcount获得插入的行数:
print('row count', cursor.rowcount)


# 提交事务:
conn.commit()

# 关闭Cursor:
cursor.close()



'''查找数据'''


cursor = conn.cursor()

# 执行查询语句:
cursor.execute('select * from user where id=%s', ('1',))

# 获得查询结果集:
values = cursor.fetchall()
print(values)

cursor.close()


#!/usr/bin/python
# -*- coding: utf-8 -*-



'''
ORM
'''

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:连接到上次在 041.py 中创建的 test 数据库
# https://stackoverflow.com/questions/22082447/sqlalchemy-cant-connect-to-local-mysql
# https://dev.mysql.com/doc/refman/5.7/en/can-not-connect-to-server.html
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test?unix_socket=/tmp/mysql.sock')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


def writeDataToDB():

    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = User(id='5', name='Bob')
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


def readDataFromDB():

    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(User).filter(User.id=='5').one()
    # 打印类型和对象的name属性:
    print('type:', type(user))
    print('name:', user.name)
    # 关闭Session:
    session.close()

writeDataToDB()
readDataFromDB()
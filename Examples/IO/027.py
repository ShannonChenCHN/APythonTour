#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
操作文件和目录
'''

import os

'''系统'''
print(os.name)
print(os.uname())


'''环境变量'''
print(os.environ)
print(os.environ.get('PYTHONPATH'))

'''操作文件和目录'''

# 查看当前目录的绝对路径
abspath = os.path.abspath('.')
print(abspath)

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
# 这里不能用 home dir 的符号 ~
joinedpath = os.path.join(abspath, 'testdir')
print(joinedpath)

# 用户目录
homedir = os.path.expanduser('~')
print(homedir)

# 判断目录是否存在
if os.path.exists(joinedpath):
    os.rmdir(joinedpath) # 删掉一个目录

# 创建一个目录
os.mkdir(joinedpath)

# 重命
newpath = joinedpath + 'new'
os.rename(joinedpath, newpath)

# 删掉一个目录
os.rmdir(newpath)

# 复制
import  shutil
licensepath = '../../LICENSE'
copypath = licensepath + 'new'
shutil.copy(licensepath, copypath)
os.remove(copypath)



# 拆分路径
print(os.path.split('/Users/michael/testdir/file.txt'))

# 扩展名
print(os.path.splitext('/path/to/file.txt'))


print([x for x in os.listdir('.') if os.path.isdir(x)])

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
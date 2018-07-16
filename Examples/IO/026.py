#!/usr/bin/python
# -*- coding: utf-8 -*-

#  StringIO

from io import StringIO

f = StringIO()
f.write('hello\n')
f.write('Hi!\n')
f.write('world!')
print(f.getvalue())


# BytesIO

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
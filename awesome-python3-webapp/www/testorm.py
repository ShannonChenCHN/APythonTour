
"""
测试 orm 代码
"""

import asyncio
import orm
from model import User, Blog, Comment

@asyncio.coroutine
def test():
    loop = asyncio.get_event_loop()
    yield from orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

for x in test():
    pass
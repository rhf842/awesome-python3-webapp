#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

import sys

from www import orm
from www.models import User


def test(loop):
    yield from orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='123456',
                               db='awesome')
    user = User(name='Test', email='test@example.com', passwd='123456', image='ablout:blank')
    print('-------create finish-----------')
    user.show()
    yield from user.save()
    yield from orm.destory_pool()



loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)

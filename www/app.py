#!/usr/local/bin python3
# -*- coding: utf-8 -*-

import logging
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>tianyaxifeng</h1>', content_type='text/html')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 8110)
    logging.info('server started at http://127.0.0.1:8110....')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

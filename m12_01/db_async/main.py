import asyncio
import sys

import aiohttp_jinja2
import jinja2
from aiohttp import web

from src.models import pg_context
from src.routes import setup_routes
from src.settings import config, BASE_DIR

app = web.Application()
app['config'] = config
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR / 'src' / 'templates')))
app.cleanup_ctx.append(pg_context)
setup_routes(app)


if __name__ == '__main__':
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    web.run_app(app)


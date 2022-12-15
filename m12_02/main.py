import asyncio
import sys
import base64

import aiohttp_jinja2
import jinja2
from aiohttp import web
from cryptography import fernet
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from src.middlewares import authorize, error_middleware
from src.routes import setup_routes
from src.settings import config, BASE_DIR
from src.store.accessor import DBAccessor

app = web.Application()

f_key = fernet.Fernet.generate_key()
print(f_key)
secret_key = base64.urlsafe_b64decode(f_key)
print(secret_key)
setup(app, EncryptedCookieStorage(secret_key))

app['config'] = config

app.middlewares.append(error_middleware)
app.middlewares.append(authorize)

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR / 'src' / 'templates')))
app.router.add_static('/static', path='src/static', name='static')
app["db"] = DBAccessor()
app["db"].setup(app)
setup_routes(app)
app["websockets"] = []


if __name__ == '__main__':
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    web.run_app(app, port=config["common"]["port"])

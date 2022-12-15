import aiohttp_jinja2
from aiohttp import web
from aiohttp_session import get_session


async def handle_404(request):
    return aiohttp_jinja2.render_template('404.html', request, {"message": f"Not found url {request.url}"}, status=404)


async def handle_500(request):
    # Пишемо в логи!
    return aiohttp_jinja2.render_template('500.html', request, {"message": "Ми працюємо над виправленням проблеми"},
                                          status=500)


@web.middleware
async def error_middleware(request, handler):
    try:
        return await handler(request)
    except web.HTTPException as ex:
        if ex.status == 404:
            return await handle_404(request)
        if ex.status == 500:
            return await handle_500(request)
        raise
    except Exception:
        request.protocol.logger.exception("Error handling request")
        return await handle_500(request)


@web.middleware
async def authorize(request, handler):
    def is_protect(path: str):
        for route in ['/chat', '/signout']:
            if path.startswith(route):
                return True
        return False

    if is_protect(request.path):
        session = await get_session(request)
        if 'user' in session:
            return await handler(request)
        else:
            raise web.HTTPForbidden(text='Іди геть розбійнику!')

    return await handler(request)

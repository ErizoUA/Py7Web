import aiohttp
from aiohttp import web
from aiohttp_jinja2 import template
from aiohttp_session import get_session

from src.store.models import User, Messages


class ChatList(web.View):
    @template('pages/chat.html')
    async def get(self):
        session = await get_session(self.request)
        auth = True if 'user' in session else False
        messages = await self.request.app["db"].messages.outerjoin(User).select().limit(25).order_by(
            Messages.created.desc()).gino.all()
        return {"title": 'Chat', "auth": auth, "messages": messages}


class WebSocket(web.View):
    async def get(self):

        ws = web.WebSocketResponse()
        await ws.prepare(self.request)

        session = await get_session(self.request)
        login = session["user"]

        for ws_ in self.request.app["websockets"]:
            await ws_.send_str(f"{login} join to the chat")

        self.request.app["websockets"].append(ws)

        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                if msg.data == 'close':
                    await ws.close()
                else:
                    user_id = int(session["user_id"])
                    await self.request.app["db"].messages.create(message=msg.data, user_id=user_id)
                    for ws_ in self.request.app["websockets"]:
                        await ws_.send_str(f"{login}: {msg.data}")
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print('ws connection closed with exception %s' %
                      ws.exception())

        self.request.app["websockets"].remove(ws)
        for ws_ in self.request.app["websockets"]:
            await ws_.send_str(f"{login} disconnected from the chat")
        print('websocket connection closed')

        return ws
#!/usr/bin/env python

import asyncio
import websockets


async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        r = await websocket.recv()
        print(f"Client: {r}")


if __name__ == '__main__':
    asyncio.run(hello())

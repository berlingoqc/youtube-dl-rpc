import asyncio
import pathlib
import websockets
import json

from queue import Queue

clients = {}

resolver = {}


def broadcast(msg):
    for _, v in clients.items():
        v.put(msg)


async def hello(websocket, path):
    print('got connection ', websocket, ' path ', path)
    queue = Queue()
    clients[websocket] = queue
    try:
        while True:
            # regarde pour un message a envoyer
            try:
                data = queue.get(timeout=0.3)
                json_data = json.dumps(data)
                print('SENDING ', json_data)
                await websocket.send(json_data)
            except:
                pass
    except websockets.exceptions.ConnectionClosed as ex:
        print('Connection closed')
        clients.pop(websocket)
    except Exception as ex:
        print('GENERIC ERROR ', ex)


def run(host, port):
    print(host, port)
    start_server = websockets.serve(hello, host, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

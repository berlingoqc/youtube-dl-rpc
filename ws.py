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
            # attend pour une message
            try:
                message = await asyncio.wait_for(websocket.recv(), timeout=0.1)
                json_data = json.loads(message)
                if 'method' in json_data and 'data' in json_data:
                    if json_data['method'] in resolver:
                        print('find resolver')
                        await resolver[json_data['method']](
                            websocket, json_data['data'])
            except asyncio.TimeoutError:
                pass
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


def run():
    start_server = websockets.serve(hello, 'localhost', 3000)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

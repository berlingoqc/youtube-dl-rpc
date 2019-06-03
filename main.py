import asyncio
import ws
import json
import downloading_thread


class YDLTImpl(downloading_thread.YoutubeDlDowloadingThread):

    def __init__(self):
        super().__init__()

    def progressHook(self, data):
        dic = {
            "event": "progress",
            "data": data
        }
        ws.broadcast(dic)


download = YDLTImpl()


async def addQueue(client, data):
    download.AddItemQueue(data)
    await client.send("proute que croute")


async def getQueue(client, data):
    print('SENDING QUEUE')
    await client.send(json.dumps(download.public_queue))


if __name__ == "__main__":
    ws.resolver['add'] = addQueue
    ws.resolver['getQueue'] = getQueue
    ws.run()

import asyncio
import rpc
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


def addQueue(data):
    download.AddItemQueue(data)
    return "OK"


def getQueue():
    return download.public_queue


if __name__ == "__main__":
    rpc.run_simple('localhost', 4000, rpc.application)
    ws.run()

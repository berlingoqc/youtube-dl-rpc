from queue import Queue
from threading import Thread
import youtube_dl
import ws


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class YoutubeDlDowloadingThread:
    worker = Thread()
    queue = Queue()
    logger = MyLogger()

    ydl_opts = {}

    isDownloading = False

    public_queue = []

    def __init__(self):
        self.worker = Thread(target=self.downloadThread)
        self.worker.setDaemon(True)
        self.worker.start()

    # PUBLIC FUNCTION

    def AddItemQueue(self, url, settings={}):
        self.queue.put(url)
        self.public_queue.append((url, settings))
        self.progressHook(self.public_queue)

    def GetQueue(self):
        return self.public_queue

    def GetSettings(self):
        return self.ydl_opts

    def SetSettings(self, opts):
        self.ydl_opts = opts

    # PRIVATE FUNCTION

    def downloadThread(self):
        while True:
            (url, settings) = self.queue.get()
            print('Downloading next item ', url)
            print('Settings ', settings)

            option = self.ydl_opts
            option['progress_hooks'] = [self.progressHook]
            option['logger'] = self.logger

            with youtube_dl.YoutubeDL(option) as ydl:
                ydl.download([url])

            self.queue.task_done()
            self.public_queue.remove(url)

    def progressHook(self, data):
        dic = {
            "event": "progress",
            "data": data
        }
        ws.broadcast(dic)


download = YoutubeDlDowloadingThread()

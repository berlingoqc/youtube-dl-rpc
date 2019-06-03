from queue import Queue
from threading import Thread
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
}


class YoutubeDlDowloadingThread:

    # variable
    worker = Thread()
    queue = Queue()
    logger = MyLogger()
    isDownloading = False

    public_queue = []

    def __init__(self):
        self.worker = Thread(target=self.downloadThread)
        self.worker.setDaemon(True)
        self.worker.start()

    def AddItemQueue(self, url, settings={}):
        self.queue.put(url)
        self.public_queue.append(url)
        self.progressHook(self.public_queue)

    def downloadThread(self):
        while True:
            url = self.queue.get()
            print('Downloading next item ', url)

            option = ydl_opts
            option['progress_hooks'] = [self.progressHook]
            option['logger'] = self.logger

            with youtube_dl.YoutubeDL(option) as ydl:
                ydl.download([url])

            self.queue.task_done()
            self.public_queue.remove(url)

    def progressHook(self, data):
        print(data)

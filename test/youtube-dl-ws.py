from __future__ import unicode_literals
import youtube_dl

from downloading_thread import YoutubeDlDowloadingThread


download = YoutubeDlDowloadingThread()
download.AddItemQueue("https://www.youtube.com/watch?v=6Db_8Oyy09w", {})
download.queue.join()

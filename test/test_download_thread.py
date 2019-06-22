import context
import unittest

from ydlrpc import downloading_thread


class TestDownloadThread(unittest.TestCase):

    def test_init(self):
        print(downloading_thread.download)
        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()

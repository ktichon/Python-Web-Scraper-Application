import threading
import wx
import time
from pubsub import pub


class Calc(threading.Thread):
    """Worker thread class."""

    def __init__(self, q):
        try:
            super().__init__()

            self.q = q

            self.finished = False
            self.count = 0
            self.num = 0
        except Exception as e:
            print(e)

    def run(self):
        """Worker thread."""
        try:
            while not self.finished:
                self.count += 1
                self.num = self.count ** 2
                print("Count:", self.count)
                self.q.put(self.data)
                wx.CallAfter(pub.sendMessage, "UpdateUI")
                # wx.CallAfter(pub.sendMessage, "UpdateUI", self.data)
                print("Num:", self.num)
                time.sleep(0.1)
            print("Worker thread finished.")
        except Exception as e:
            print(e)

    def start_work(self):
        """Start worker thread."""
        try:
            self.start()
        except Exception as e:
            print(e)

    def stop_work(self):
        """Set signal to stop worker thread."""
        try:
            self.finished = True
        except Exception as e:
            print(e)

    @property
    def data(self):
        """Return dictionary of current values."""
        try:
            d = {}
            d["count"] = self.count
            d["num"] = self.num
            return d
        except Exception as e:
            print(e)
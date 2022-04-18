import threading
import random
import time
from pubsub import pub


class Calc(threading.Thread):

    def __init__(self):
        super().__init__()
        self.finished = False
    
    def run(self):
        while not self.finished:
            ans = self.calc_something()
            pub.sendMessage('calc', ans=ans)
            time.sleep(10)

    def calc_something(self):
        ans = random.randint(10, 30)
        time.sleep(ans)
        return ans
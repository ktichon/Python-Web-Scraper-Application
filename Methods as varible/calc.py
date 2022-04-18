"""Calculates some things."""
import time
import random

class Calc():
    """Performs math operations."""

    def __init__(self):
        self.calc_done = None
        self.answer = 0

    def calc_something(self):
        """Calculates nothing."""
        try:
            time.sleep(10)
            self.answer = random.randint(0, 100)
            self.calc_done()
        except Exception as e:
            print(e)

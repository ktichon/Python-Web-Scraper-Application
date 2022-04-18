"""Calculates some things."""
import time
import random

class Calc():
    """Performs math operations."""

    def __init__(self, id):
        """Init method."""
        try:
            self.calc_done = None
            self.id = id
        except Exception as e:
            print(e)

    def calc_something(self):
        """Calculates nothing."""
        try:
            print(f"Instance #{self.id}: Starting calculation...")
            answer = random.randint(10, 30)
            time.sleep(answer)
            self.calc_done(self.id, answer)
        except Exception as e:
            print(e)

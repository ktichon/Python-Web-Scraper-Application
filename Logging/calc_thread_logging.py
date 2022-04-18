"""Calculates some things."""
import time
import random
import logging

class Calc():
    """Performs math operations."""

    logger = logging.getLogger("main." + __name__)

    def __init__(self, id):
        """Init method."""
        try:
            self.calc_done = None
            self.id = id
        except Exception as e:
            self.logger.error(f"Calc:init:{e}")

    def calc_something(self):
        """Calculates nothing."""
        try:
            print(f"Instance #{self.id}: Starting calculation...")
            self.logger.info(f"Instance #{self.id}: Starting calculation...")
            answer = random.randint(10, 30)
            time.sleep(answer)
            self.calc_done(self.id, answer)
        except Exception as e:
            self.logger.error(f"Calc:calc_something:{e}")

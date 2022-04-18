"""Threading demonstration module."""
from calc_thread_logging import Calc
import threading
import logging
import logging.handlers

myLock = threading.RLock()


def done_calc(id: int, answer: int):
    """Calc finished event."""
    with myLock:
        try:
            print(f"Instance #{id}: Answer is: {answer}")
            logger.info(f"Instance #{id}: Answer is: {answer}")
        except Exception as e:
            logger.error(f"main_thread:done_calc:{e}")


if __name__ == "__main__":
    try:
        logger = logging.getLogger("main")
        logger.setLevel(logging.DEBUG)
        fh = logging.handlers.RotatingFileHandler(filename="threads.log",
                                                  maxBytes=10485760,
                                                  backupCount=10)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info("Main Thread Started")

        mycalc1 = Calc(1)
        mycalc2 = Calc(2)
        mycalc3 = Calc(3)

        mycalc1.calc_done = done_calc
        mycalc2.calc_done = done_calc
        mycalc3.calc_done = done_calc

        t1 = threading.Thread(target=mycalc1.calc_something)
        t2 = threading.Thread(target=mycalc2.calc_something)
        t3 = threading.Thread(target=mycalc3.calc_something)

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()
        print("End of demo.")
    except Exception as e:
        logger.error(f"main_thread:main:{e}")

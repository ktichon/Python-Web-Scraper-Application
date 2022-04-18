"""Threading demonstration module."""
from calc_thread import Calc
import threading


def done_calc(id: int, answer: int):
    """Calc finished event."""
    try:
        print(f"Instance #{id}: Answer is: {answer}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
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
        print(e)

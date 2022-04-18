from pubsub import pub
from calc_thread2 import Calc


def done(ans):
    print("The answer is:", ans)
    if ans == 10:
        mycalc.finished = True
        print("Finished calculations! Terminating application.")


pub.subscribe(done, 'calc')

mycalc = Calc()
mycalc.start()

from calc import Calc


def done_calc():
    try:
        print(f"Finished calculating. Answer is: {mycalc.answer}")
    except Exception as e:
        print(e)

if __name__=="__main__":
    try:
        mycalc = Calc()
        mycalc.calc_done = done_calc
        mycalc.calc_something()
    except Exception as e:
        print(e)

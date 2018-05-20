
def fact(numb):
    if isinstance(numb, int) and numb >= 0:
        if numb < 2:
            return 1
        else:
            return numb * fact(numb - 1)
    else:
        raise ValueError

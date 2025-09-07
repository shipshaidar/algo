
def fast_expt(a: int, p: int) -> int:
    s: int = 1
    while p != 0:
        if (p % 2 == 0):
            p //= 2
            a **= 2
        else:
            p -= 1
            s *= a
    return s

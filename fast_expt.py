 # Попробуйте сравнить fast_expt(2, 1000) и 2 ** 1000
 
def fast_expt(a: int, p: int) -> int:
    # a основание степени
    # p показатель степени
    # s состояние (сохраняет инвариант sa**p)
    s: int = 1
    while p != 0:
        if (p % 2 == 0):
            p //= 2
            a **= 2
        else:
            p -= 1
            s *= a
    return s

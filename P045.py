import numpy as np
from eulertools import timeit


def pentn(n):
    a = n * (3 * n - 1) / 2
    return a


def pent(n):
    a = int(n * (3 * n - 1) / 2)
    return a


def ispent(a):
    n = 1 / 6 * ((24 * a + 1) ** (1 / 2) + 1)
    return n - int(n) == 0


def trin(n):
    a = n * (n + 1) / 2
    return a


def hexn(n):
    a = n * (2 * n - 1)
    return a


@timeit
def problem():
    # a = np.arange(150, 600000)
    # h = hexn(np.arange(0, 15000))
    # t = trin(np.arange(0, 600000))
    # p = pentn(np.arange(0, 600000))
    h = set([hexn(x) for x in range(1, 600000)])
    t = set([trin(x) for x in range(1, 600000)])
    p = set([pentn(x) for x in range(1, 600000)])

    # print(p[:50])
    count = 0
    for i, hn in enumerate(h):
        if hn in p:
            if hn in t:
                print(i, hn)
                count = count + 1
                if count == 6:
                    return i, hn


if __name__ == "__main__":
    print(problem())
    print(ispent(4128501))

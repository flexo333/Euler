def pentn(n):
    a = n * (3 * n - 1) / 2
    return a


def trin(n):
    a = n * (n + 1) / 2
    return a


def hexn(n):
    a = n * (2 * n - 1)
    return a


import numpy as np


def problem():
    a = np.arange(150, 600000)
    h = hexn(np.arange(0, 1500))
    # t = trin(np.arange(0,600000))
    p = pentn(np.arange(0, 600000))

    count = 0
    for i, hn in enumerate(p):
        if hn in h:
            # if hn in p:
            print(i, hn)
            count = count + 1
            if count == 4:
                break
    # print t.argwhere(4128501)
    # print np.extract(4128501,h)
    # print t[11326]
    # t 2873 4128501
    # p 567561
    # h 1437

    # 1533776805

    # 4128501
    print(pentn(567561))
    print(trin(2873))

    print(hexn(1437))
    print(p[:6])


if __name__ == "__main__":
    print(problem())

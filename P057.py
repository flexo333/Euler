import eulertools as et
from eulertools import timeit

"""
Square root convergents
1 + 1/2
"""


def sqrt2():
    numerat, denomin = (3, 2)
    for x in range(1, 1001):
        numerat, denomin = numerat + 2 * denomin, numerat + denomin

        r = len(str(numerat)) > len(str(denomin))
        yield r

@timeit
def problem():
    x = sqrt2()
    return sum(y for y in x)


if __name__ == "__main__":
    print(problem())
    # print(reverse_and_add(63))
    # print(reverse_and_add(123))
    # print(reverse_and_add(334))

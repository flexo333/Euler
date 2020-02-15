import eulertools as et
from eulertools import timeit

"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""


@timeit
def problem():
    return str(sum(i**i for i in range(1, 1000)))[-10:]


if __name__ == "__main__":
    print(problem())
    # 'problem'  148043.22
#     123.75 sec

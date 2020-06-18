import eulertools as et
from eulertools import timeit

"""
0 = 1,1 - 1
1 = 2,3 - 3 5 7 9
2 = 4,5 - 13 17 21 25
3 = 6,7 - 31 37 43 49

"""


def corner_values(n):
    if n == 0:
        return [1]
    last_corner = ((n * 2) + 1)**2
    corner_count = [3, 2, 1, 0]
    return list(last_corner - (n * 2) * x for x in corner_count)


@timeit
def problem2():
    # diagonal_values = list()
    prime_count = 0
    total_count = 1
    for i in range(1, 6):
        new_corners = corner_values(i)
        prime_count += sum(et.is_prime(v) for v in new_corners)
        total_count += len(new_corners)
        ratio = prime_count / total_count
        if (ratio > 0.1) or i % 500 == 0:
            print('{}: {} --> {} {}'.format(i, ratio,prime_count,total_count))
        if (ratio < 0.1):
            return i
        # print(diagonal_values)


@timeit
def problem():
    # diagonal_values = list()
    prime_count = 0
    total_count = 1
    for i in range(1, 50000):
        new_corners = corner_values(i)
        prime_count += sum(et.is_prime(v) for v in new_corners)
        total_count += len(new_corners)
        ratio = prime_count / total_count
        if (ratio < 0.1) or i % 500 == 0:
            print('{}: {} --> {} {}'.format(i, ratio,prime_count,total_count))
        if (ratio < 0.1):
            return i * 2 + 1
        # print(diagonal_values)





if __name__ == "__main__":
    print(problem())
    # print(corner_values(0))
    # print(corner_values(1))
    # print(corner_values(2))
    # print(corner_values(3))
    # print(corner_values(4))

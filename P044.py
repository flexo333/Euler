from itertools import combinations, permutations

import log

from eulertools import timeit

LOG = log.get_logger(__name__)

PENTAGONALS = [int(n * (3 * n - 1) / 2) for n in range(1, 20000)]


def pent(n):
    a = int(n * (3 * n - 1) / 2)
    return a


def ispent(a):
    n = 1 / 6 * ((24 * a + 1) ** (1 / 2) + 1)
    return n == int(n)


def lexi(number_l, n=-1):
    number_list = number_l
    if n == 0:
        yield ""
    elif len(number_list) <= 1:
        yield str(number_list[0])
    else:
        for x in number_list:
            for y in lexi([i for i in number_list if i != x], n - 1):
                yield str(x) + "," + str(y)


@timeit
def pent_dict():
    pent_d = {}
    pent_num = {}
    for p in range(1, 1000):
        pent_d[pent(p)] = p
        pent_num[p] = pent(p)
    return pent_d, pent_num


def problem():
    pentagonal_pairs = combinations(PENTAGONALS, 2)
    result_set = []
    for pair in pentagonal_pairs:
        if ispent(sum(pair)) and ispent(abs(pair[0]-pair[1])):
            LOG.info(f'This is a pentagonal pair: {pair}')
            result_set.append(pair)

    return min(abs(p[0]-p[1]) for p in result_set)


if __name__ == "__main__":
    print((problem()))


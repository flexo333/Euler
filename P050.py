from collections import defaultdict
from itertools import combinations

import eulertools as et
from eulertools import timeit
import log

LOG = log.get_logger(__file__)
prime_list = list(p for p in et.primeseive(1000000))
prime_set = set(prime_list)
prime_list = list(i for i in prime_list if i < 150000)
prime_loop = list(i for i in prime_list if i < 150)


@timeit
def problem():
    longest_run = 1
    for i, item in enumerate(prime_loop):
        for x in range(longest_run, 1000):
            if len(prime_list) > i + x:
                test_sum = sum(prime_list[i: i + x])
                if test_sum < 1000000:
                    if test_sum in prime_set:
                        if longest_run < x:
                            longest_run = x
                            LOG.info(f'New Longest run is {x}, prime is {test_sum}')
                            LOG.info(f'The prime_list is: {(prime_list[i: i + x])}')


if __name__ == "__main__":
    print(problem())


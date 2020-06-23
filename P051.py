from collections import defaultdict
from itertools import combinations

import eulertools as et
from eulertools import timeit
import log

LOG = log.get_logger(__file__)
prime_list = list(p for p in et.primeseive(1000000))


@timeit
def problem():
    pass



if __name__ == "__main__":
    print(problem())


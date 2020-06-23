from collections import defaultdict
from itertools import combinations

import eulertools as et
from eulertools import timeit
import log

LOG = log.get_logger(__file__)



@timeit
def problem():
    prime_list = list(p for p in et.primeseive(9999))# if p > 1000)

    # prime_sets = list(''.join(sorted(str(p))) for p in prime_list)

    primes = defaultdict(list)

    for prime in prime_list:
        primes["".join(sorted(str(prime)))].append(prime)
    filtered_dictionary = {
        key: value for key, value in primes.items() if len(value) > 2
    }

    LOG.info(f"Options before filtering is {len(primes.keys())}")
    LOG.info(f"Options with 3 or more #'s is {len(filtered_dictionary.keys())}")

    for k, v in primes.items():
        for combo in combinations(v, 3):
            sorted_combo = sorted(combo)
            if sorted_combo[1] - sorted_combo[0] == sorted_combo[2] - sorted_combo[1]:
                LOG.info(f"The combo is:{sorted_combo}")
                return_val = sorted_combo
    return ''.join(str(i) for i in return_val)


if __name__ == "__main__":
    print(problem())
    # 'problem'  148043.22
#     123.75 sec

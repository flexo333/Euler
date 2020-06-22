from collections import defaultdict


import eulertools as et
from eulertools import timeit
import logging

logging.basicConfig(level=logging.DEBUG)



"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
 is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the
 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""


@timeit
def problem():
    prime_list = et.primeseive(9999)
    prime_list = list(p for p in prime_list if p > 1000)
    test = list(p for p in prime_list if ''.join(sorted(str(p))) == '1478')
    logging.debug(f'Filtered List{test}')

    prime_sets = list(''.join(sorted(str(p))) for p in prime_list)

    primes = defaultdict(list)

    for prime in prime_list:
        if prime > 1000:
            primes[''.join(sorted(str(prime)))].append(prime)
    print_string = primes['1478']
    logging.debug(f'primedict    {print_string}')

    logging.debug(len(prime_sets))
    logging.debug(prime_sets[:5])



if __name__ == "__main__":
    print(problem())
    # 'problem'  148043.22
#     123.75 sec


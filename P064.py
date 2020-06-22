# import eulertools as et
from eulertools import timeit
from itertools import combinations, permutations

import log

LOG = log.get_logger(__file__)

"""
"""


@timeit
def problem():
    summer = 0
    for i in range(1, 25):
        LOG.debug(f"{i}, {i**2}")
        summer += i**2

    return summer


if __name__ == "__main__":
    result = problem()
    print(result)

    LOG.warning("Watch out!")  # will print a message to the console
    LOG.info("I told you so")  # will not print anything

# import eulertools as et
from eulertools import timeit
from itertools import combinations, permutations

import logging

FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.DEBUG) # better to have too much log than not enough

    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())

    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False

    return logger

"""
"""
# import eulertools as et
from eulertools import timeit
from itertools import combinations, permutations

"""
"""

def problem():
    summer = 0
    for i in range(1, 25):
        print(f'{i}, {power_count(i)}')
        summer += power_count(i)

    return summer


if __name__ == "__main__":
    # result = problem()
    # print(result)

    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything






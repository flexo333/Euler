# import eulertools as et
from eulertools import timeit
from itertools import combinations, permutations

"""
"""
# import eulertools as et
from eulertools import timeit
from itertools import combinations, permutations

"""
"""


def power_count(n):
    counter = 0
    for x in range(1, 1000):
        z = x ** n
        if len(str(z)) == n:
            counter += 1
        if len(str(z)) > n:
            return counter

@timeit
def problem():
    summer = 0
    for i in range(1, 25):
        print(f'{i}, {power_count(i)}')
        summer += power_count(i)

    return summer




if __name__ == "__main__":
    result = problem()
    print(result)


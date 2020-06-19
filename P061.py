# import eulertools as et
from eulertools import timeit
from itertools import combinations, permutations

"""
"""

TRIANGLES = [int(n * (n + 1) / 2) for n in range(150) if 999 < n * (n + 1) / 2 < 9999]
SQUARES = [n ** 2 for n in range(110) if 999 < n ** 2 < 9999]
PENTAGONALS = [int(n * (3 * n - 1) / 2) for n in range(100) if 999 < n * (3 * n - 1) / 2 < 9999]
HEXAGONALS = [n * (2 * n - 1) for n in range(100) if 999 < n * (2 * n - 1) < 9999]
HEPTAGONALS = [int(n * (5 * n - 3) / 2) for n in range(100) if 999 < n * (5 * n - 3) / 2 < 9999]
OCTAGONALS = [n * (3 * n - 2) for n in range(100) if 999 < n * (3 * n - 2) < 9999]

print(len(TRIANGLES), len(SQUARES), len(PENTAGONALS), len(HEXAGONALS), len(HEPTAGONALS), len(OCTAGONALS))


def is_cyclical(n, m):
    if n%100 == int(m / 100):
        return True
    else:
        return False

cycles = (TRIANGLES, SQUARES, PENTAGONALS, HEXAGONALS, HEPTAGONALS, OCTAGONALS)


@timeit
def problem():
    for combo in permutations(cycles, 6):


        for a in combo[0]:
            for b in combo[1]:
                if is_cyclical(a, b):
                    for c in combo[2]:
                        if is_cyclical(b, c):
                            for d in combo[3]:
                                if str(c)[-2:] == str(d)[0:2]:
                                    for e in combo[4]:
                                        if str(d)[-2:] == str(e)[0:2]:
                                            for f in combo[5]:
                                                if str(e)[-2:] == str(f)[0:2]:
                                                    if str(f)[-2:] == str(a)[0:2]:
                                                        print(a, b, c, d, e, f)
                                                        print(a + b + c + d + e + f)


if __name__ == "__main__":
    result = problem()
    print(result)


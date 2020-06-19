# import eulertools as et
from eulertools import timeit

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

@timeit
def problem():
    for triangle in TRIANGLES:
        for square in SQUARES:
            if is_cyclical(triangle, square):
                for pentagonal in PENTAGONALS:
                    if is_cyclical(square, pentagonal):
                        for hexagonal in HEXAGONALS:
                            if str(pentagonal)[-2:] == str(hexagonal)[0:2]:
                                for heptagonal in HEPTAGONALS:
                                    if str(hexagonal)[-2:] == str(heptagonal)[0:2]:
                                        for octagonal in OCTAGONALS:
                                            if str(heptagonal)[-2:] == str(octagonal)[0:2]:
                                                # if str(octagonal)[-2:] == str(triangle)[0:2]:
                                                print(triangle, square, pentagonal, hexagonal, heptagonal, octagonal)


if __name__ == "__main__":
    result = problem()
    print(result)


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

CUBE_LIST = list((tuple([''.join(sorted(str(x ** 3))), x ** 3]) for x in range(10000)))
print(f'Cubes Lengeth {len(CUBE_LIST)}')

@timeit
def problem():

    for cube in CUBE_LIST:
        if len(list(x for x in CUBE_LIST if x[0] == cube[0])) == 5:
            print (cube)

if __name__ == "__main__":
    result = problem()
    print(result)


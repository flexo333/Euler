import eulertools as et
from eulertools import timeit

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
    prime_sets = (set((c for c in str(p)) for p in prime_list if p > 1000))
    for int_set in prime_sets:
        prime_permutations = [x for x in prime_list if set((c for c in str(x))) == set((c for c in str(int_set)))]
        if len(prime_permutations) == 3:
            print(prime_permutations)
    print(len(prime_sets))
    return len(prime_sets)






if __name__ == "__main__":
    print(problem())
    # 'problem'  148043.22
#     123.75 sec

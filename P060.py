import eulertools as et
from eulertools import timeit

from itertools import combinations, permutations
from itertools import chain

"""
Square root convergents
1 + 1/2
"""


@timeit
def ps(n):
    primes = et.primeseive(n)
    primes.remove(2)
    return primes


def prime_pair(p):
    a, b = p
    test_number = int(str(a) + str(b))
    test_number_reverse = int(str(b) + str(a))
    return et.is_prime(test_number) and et.is_prime(test_number_reverse)


@timeit
def generate_prime_pairs(pairs):
    pairs_primes = {pair: prime_pair(pair) for pair in pairs}
    return pairs_primes


@timeit
def generate_prime_sets(primes_set, set_length):
    """
    Get all combinations of prime_sets
    and length set_length
    :rtype: tuple
    """
    comb = combinations(primes_set, set_length)
    pairs = combinations(primes_set, 2)

    pairs_primes = generate_prime_pairs(pairs)

    prime_sets = []
    # Loop through all combinations, adding those
    # that are prime sets to the list.
    for i in comb:
        if all(pairs_primes[p] for p in combinations(i, 2)):
            # print(i)
            prime_sets.append(set(i))

    return prime_sets



@timeit
def problem_1():
    primes = ps(2000)
    primes_set = set(primes)

    # A Python program to print all
    # combinations of given length
    from itertools import combinations, permutations

    # Get all combinations of [1, 2, 3]
    # and length 2
    comb = combinations(primes_set, 5)
    # print(len(list(comb)))
    # Print the obtained combinations
    for i in comb:
        if all(prime_pair(p) for p in permutations(i, 2)):
            print(i)
            return i


@timeit
def problem():
    primes = sorted(list(set(ps(8000))))
    print('The number of primes is {}'.format(len(primes)))
    # A Python program to print all
    # combinations of given length

    prime_set_list = generate_prime_sets(primes, 3)

    numbs = set((chain.from_iterable(prime_set_list)))
    print('The number of primes in {} item sets is {}'.format(3, len(numbs)))
    print('The number of prime pair sets is {}'.format(len(prime_set_list)))
    print(f'The first five prime pair sets are {prime_set_list[:4]}')

    # Convert list of prime sets into 1 group higher.
    print('Convert to sets of 4')

    my_sets = (p[0].union(p[1]) for p in combinations(prime_set_list, 2))
    my_lists = [list(x) for x in my_sets if len(x) == 4]

    # my_sets = (p[0].union(p[1]) for p in combinations(prime_set_list, 2))
    # my_lists = []
    #
    # for p in combinations(prime_set_list, 2):
    #     combination_list = p[0].union(p[1])
    #     # combination_list = p
    #     if len(combination_list) == 4:
    #         if combination_list in my_lists:
    #             my_lists.append(list(combination_list))

    print(len(my_lists))
    new_list = []
    for my_set in my_lists:
        if all(prime_pair(p) for p in permutations(my_set, 2)):
            new_list.append(tuple(my_set))
            # print(my_set)

    print('The length before is {}'.format(len(new_list)))
    new_list = list(set(new_list))
    print('The length after is {}'.format(len(new_list)))
    new_list = list(set(x) for x in new_list)

    print('Convert to sets of 5')

    my_sets = (p[0].union(p[1]) for p in combinations(new_list, 2))
    my_lists = [list(x) for x in my_sets if len(x) == 5]

    print(len(my_lists))
    new_list = []
    for my_set in my_lists:
        if all(prime_pair(p) for p in permutations(my_set, 2)):
            new_list.append(my_set)
            print(my_set)


if __name__ == "__main__":
    print(problem())
    # print(168*167*166)

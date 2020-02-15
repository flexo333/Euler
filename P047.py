import eulertools as et
from eulertools import timeit

"""
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""


@timeit
def problem():
    print(f'Generating prime_list')
    prime_list = et.primeseive(100000)
    print(f'Generated prime_list')

    for i in range(129000, 500000):
        if not any(x in prime_list for x in [i, i + 1, i + 2, i + 3]):
            if i%10000==0: print(f'testing i: {i} and still going')
            if len(set(et.factorise(prime_list, i))) == 4:
                if len(set(et.factorise(prime_list, i + 1))) == 4:
                    if len(set(et.factorise(prime_list, i + 2))) == 4:
                        if len(set(et.factorise(prime_list, i + 3))) == 4:
                            print(f'this is did it {i}')
                            return i

@timeit
def problem2():
    print(f'Generating prime_list')
    prime_list = et.primeseive(100000)
    print(f'Generated prime_list')

    for i in range(1, 500000):
        if i%10000==0: print(f'testing i: {i} and still going')
        consec_num = 0
        while consec_num != 4:
            if len(set(et.factorise(prime_list, i))) == 4:
                consec_num += 1
            else:
                consec_num = 0
            i += 1
        return i - 4


# *******
# Alternate Code
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 or n % int(n / i) == 0: return False
    return True


def find_dist_prime_factor(n):
    if is_prime(n): return 0
    dist_fact_list = []
    d = 2
    while d <= n and len(dist_fact_list) != 4 and not (d > int(n ** 0.5) + 1 and len(dist_fact_list) != 3):
        if is_prime(d) and n % d == 0:
            n /= d
            if d not in dist_fact_list: dist_fact_list.append(d)
        elif d != 2:
            d += 2
        else:
            d += 1
    return len(dist_fact_list)


def problem3():
    consec_num, i = 0, 1
    while consec_num != 4:
        if find_dist_prime_factor(i) == 4:
            consec_num += 1
        else:
            consec_num = 0
        i += 1
    return i - 4





if __name__ == "__main__":
    print(problem2())
    # 'problem'  148043.22
#     123.75 sec


x = problem3()
print(x)

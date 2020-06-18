import eulertools as et
from eulertools import timeit

"""
Max Power Digit Sum
"""


def digit_sum(x):
    return sum(int(d) for d in str(x))


def a_power_b(a,b):
    return a**b


@timeit
def problem():
    a_list = range(1, 100)
    b_list = range(1, 101)
    cat_list = [(a_temp, b_temp) for a_temp in a_list for b_temp in b_list]
    return max([digit_sum(a_power_b(a,b)) for a,b in cat_list])
    # return sum(rev_add_pal(x) for x in range(1, 10000))



if __name__ == "__main__":
    print(problem())
    # print(reverse_and_add(63))
    # print(reverse_and_add(123))
    # print(reverse_and_add(334))

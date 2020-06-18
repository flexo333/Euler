import eulertools as et
from eulertools import timeit

"""
Rev and Add
"""


def is_palindrome(palindrome_number):
    palindrome_number_str = str(palindrome_number)
    return palindrome_number_str == palindrome_number_str[::-1]


def reverse_and_add(n):
    rev_n = int(str(n)[::-1])
    return n + rev_n


def rev_add_pal(x_start):
    x = x_start
    i = 1
    while i < 51:
        xr = reverse_and_add(x)
        if is_palindrome(xr):
            # print("{} returns a prime after {} iterations. The prime is {}".format(x_start,i,xr))
            return False
        x = xr
        i += 1

    # print("{} fails to return a prime after {} iterations.".format(x_start,i-1))
    return True


@timeit
def problem():
    # for x in range(1, 10000):
    #     rev_add_pal(x)
    return sum(rev_add_pal(x) for x in range(1, 10000))



if __name__ == "__main__":
    print(problem())
    # print(reverse_and_add(63))
    # print(reverse_and_add(123))
    # print(reverse_and_add(334))

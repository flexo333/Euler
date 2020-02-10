# import logging


def pent(n):
    a = n * (3 * n - 1) / 2
    return a


def ispent(a):
    n = 1 / 6 * ((24 * a + 1) ** (1 / 2) + 1)
    return n


def lexi(number_l, n=-1):
    number_list = number_l
    if n == 0:
        yield ''
    elif len(number_list) <= 1:
        yield str(number_list[0])
    else:
        for x in number_list:
            for y in lexi([i for i in number_list if i != x], n - 1):
                yield str(x) + ',' + str(y)


def pent_dict():
    pent_d = {}
    pent_num = {}
    for p in range(1, 1000):
        pent_d[pent(p)] = p
        pent_num[p] = pent(p)
    return pent_d, pent_num



def problem():

        print(i)
        print(pent(a), pent(b))


if __name__ == "__main__":
    print((problem()))
    f = [i for i in lexi(range(1,10),2)]
    print(f)

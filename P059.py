import eulertools as et
from eulertools import timeit

"""
0 = 1,1 - 1
1 = 2,3 - 3 5 7 9
2 = 4,5 - 13 17 21 25
3 = 6,7 - 31 37 43 49

"""


def encrypt(array, key):
    e = []
    for i in range(0, len(array)):
        e.append(chr(array[i] ^ int(key[i % len(key)])))
    return e

def cipher():
    with open(r'C:\Code\Euler\p059_cipher.txt') as f:
        y = f.read()
    cipher_list = [int(i) for i in y.split(',')] 
    return cipher_list


def trial_code():
    cipher_list = cipher()
    cipher_list_1 = [b for a, b in enumerate(cipher_list) if a % 3  == 0]
    cipher_list_2 = [b for a, b in enumerate(cipher_list) if a % 3 - 1 == 0]
    cipher_list_3 = [b for a, b in enumerate(cipher_list) if a % 3 - 2 == 0]

    lower_case_letters = list(range(97,123))

    length_l = len(cipher_list_1)
    print(length_l)



    for lower_case_letter in lower_case_letters:
        t = sum((32 <= lower_case_letter ^ c <= 90) or (97 <= lower_case_letter ^ c <= 122) for c in cipher_list_1)
        length_l = len(cipher_list_1)
        if t == length_l:
            print(t,chr(lower_case_letter))

    length_l = len(cipher_list_2)
    print(length_l)

    for lower_case_letter in lower_case_letters:
        t = sum((32 <= lower_case_letter ^ c <= 90) or (97 <= lower_case_letter ^ c <= 122) for c in cipher_list_2)
        length_l = len(cipher_list_2)
        if t > 470:
            print(t,chr(lower_case_letter))

    length_l = len(cipher_list_3)
    print(length_l)

    for lower_case_letter in lower_case_letters:
        t = sum((32 <= lower_case_letter ^ c <= 90) or (97 <= lower_case_letter ^ c <= 122) for c in cipher_list_3)
        length_l = len(cipher_list_3)
        if t > 470:
            print(t,chr(lower_case_letter))



@timeit
def problem():
    cipher_list = cipher()
    key = [ord('e'), ord('x'), ord('p')]
    message = encrypt(cipher_list, key)
    print(''.join(message))

    print(sum(ord(x) for x in message))


if __name__ == "__main__":
    print(problem())
    # trial_code()
    # print(corner_values(0))
    # print(corner_values(1))
    # print(corner_values(2))
    # print(corner_values(3))
    # print(corner_values(4))

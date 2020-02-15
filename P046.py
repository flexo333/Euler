import eulertools as et

"""9 = 7 + 2×12
"""


def problem():
    primes = set(et.primeseive(10000))

    odds = set(range(3, 10000, 2))
    # primes = set(primes)

    composites = (primes ^ odds) & odds

    composites = list(composites)
    primes = list(primes)

    for composite in composites:
        test = [composite - prime for prime in primes if composite - prime > 0]
        r = [t for t in test if int((t / 2) ** 0.5 + 0.5) ** 2 == t / 2]
        if len(r) == 0:
            return composite

    return None


if __name__ == "__main__":
    print(problem())
    print(et.is_prime(9))

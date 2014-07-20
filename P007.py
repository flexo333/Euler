# 10001st prime
# Problem 7
# Published on 28 December 2001 at 06:00 pm [Server Time]
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def problem():
	import eulertools
	prime_list = eulertools.primeseive(120000)
	return prime_list[10000]

if __name__ == "__main__":
	# Load_MREPOS()
	problem()
	
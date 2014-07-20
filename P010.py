import eulertools as et

def problem():
	list_primes = et.primeseive(2*10**6)
	sum =0 
	for num in list_primes:
		sum += num
	return sum



if __name__ == "__main__":
	# Load_MREPOS()
	problem()


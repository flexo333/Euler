def problem():
	# The prime factors of 13195 are 5, 7, 13 and 29.

	# What is the largest prime factor of the number 600851475143 ?
	factors = []
	print 5* 7* 13 * 29

	numt = 600851475143

	i = 2
	while True:
			if numt%i==0:
				numt = numt / i
				factors.append(i)
				if numt == 1:
					break
			i += 1

	print factors


if __name__ == "__main__":
	# Load_MREPOS()
	problem()
	
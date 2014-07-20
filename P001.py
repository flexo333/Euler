def problem():
	# Problem 1
	# Published on 05 October 2001 at 06:00 pm [Server Time]
	# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

	# Find the sum of all the multiples of 3 or 5 below 1000.

	import eulertools

	sumn = 0 
	for x in xrange(1,1000):
		if x%3==0:
			sumn += x
		elif x%5==0:
				sumn += x
		else:
			pass


	return sumn


if __name__ == "__main__":
	# Load_MREPOS()
	problem()
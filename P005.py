def problem():
	import eulertools

	minresults = 0
	x=eulertools.product(eulertools.primeseive(20))
	step_size=x
	print x
	divisors=0
	n=0


	while divisors<20:
		divisors=0
		for y in xrange(1,21):
			if x%y==0:
				if y==1:
					divisors=1
				else:
					divisors+=1
			else:
				break
		if divisors==20:
				print divisors
				print x
				break
		x+=step_size
		n+=1



	print "   "

	print minresults
	print divisors
	print n
	

if __name__ == "__main__":
	# Load_MREPOS()
	problem()
	
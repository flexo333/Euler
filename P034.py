def fact(n):
	prod = 1
	for x in xrange(1,n+1):
		prod *= x
	return prod

def problem():
	sumfact = 0
	for n in range(3,3000000):
		sum_factn = 0
		for i in str(n):
			sum_factn += fact(int(i))
		if sum_factn == n:
			sumfact +=n

	return sumfact





if __name__ == "__main__":
	print problem()	
import eulertools as et

def d(n,PrimeList):
	if n == 0:
		return 0
	my_factors = et.factorise(PrimeList, n)
	sums = sum(divisors_pairs(my_factors)[:-1])
	return sums
	# for y in set(my_factors):
	# 		factors_len *= (my_factors.count(y)+1)


def divisors_pairs(factors):
	facts = factors
	u_factors = set(factors)

	iter_facts = [[x,facts.count(x)] for x in u_factors]
	divisors = []
	for item in iter_pairs(iter_facts):
		divisors += [item]
	return divisors

		
def iter_pairs(pairs):
	if len(pairs)==1:
		pairs
		for y in xrange(pairs[0][1]+1):
			yield pairs[0][0]**y
		
	else:		
		for i in pairs[0:1]:
			for y in xrange(i[1]+1):
				for z in  iter_pairs(pairs[1:]):
					yield (i[0]**y) * z 


def problem2():
	# print d(8)
	# print d(7)
	PrimeList = et.primeseive(10001)

	sumn = 0
	for i in xrange(1,10001):

		di = d(i,PrimeList)
		ddi = d(di,PrimeList)
		if i == ddi and not i == di:
		 	sumn += i
	print sumn

def d2(n):
    if n == 0:
    	return 0
    x =  set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
    return sum(x) - n

def problem():
	# print d(8)
	# print d(7)
	# PrimeList = et.primeseive(10001)

	sumn = 0
	for i in xrange(1,10001):

		di = d2(i)
		ddi = d2(di)
		if i == ddi and not i == di:
		 	sumn += i
	return sumn

if __name__ == "__main__":
	problem()
	# print iterative_factorial(5)
	# import eulertools as et




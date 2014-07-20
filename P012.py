import eulertools as et

def prime_facts(fn_num_1, fn_nnum_2, PrimeList):
	factors_1 = et.factorise(PrimeList, fn_num_1)
	if len(factors_1)==0:
		factors_1 += [fn_num_1]

	factors_2 = et.factorise(PrimeList, fn_nnum_2)
	if len(factors_2)==0:
		factors_2 += [fn_nnum_2]
	
	factors = factors_1 + factors_2
	return factors

def problem():
	max_len = 0
	P_List_1 = et.primeseive(50)
	for n in xrange(1, 15000, 1):
		num_1 = int(n/2 ) + n%2
		num_2 = 2 * int(n/2) + n%2 
		my_factors = prime_facts(num_1, num_2,P_List_1)
		
		factors_len = 1
		for y in set(my_factors):
			factors_len *= (my_factors.count(y)+1)

		if factors_len>500:
			return num_1 * num_2
			break

if __name__ == "__main__":
		print problem()
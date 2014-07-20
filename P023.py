def problem():
	abundant = []
	for n in xrange(1, 28124):
		items = set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
		items.discard(n)
		if sum(items)>n: abundant.append(n)
	# print abundant

	abund_pairs = set(x + y for x in abundant for y in abundant)

	

	not_abund_pairs = list(x for x in xrange(1,28124) if x not in abund_pairs)
	return sum(not_abund_pairs)



if __name__ == "__main__":
	problem()

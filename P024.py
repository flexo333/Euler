def lexi(number_l):
	number_list = number_l
	if len(number_list)<=1:
		yield str(number_list[0])
	else:
		for x in number_list:
			for y in lexi([i for i in number_list if i != x]):
				yield str(x) + str(y)
				

def fact(n):
	prod = 1
	for x in xrange(11-n,n+1):
		prod *= x
	return prod


def problem():
	# print map(int,lexi(list([3,5,8,9])))
	# for item in lexi([3,5,8,9]):
	# 	print item
	# for i in xrange(p):
	my_list = [fact(i) for i in xrange(10,0,-1)]
	test = 10
	my_counts = []
	for item in my_list:
		x,y = divmod(test,item)
		my_counts.append(x)
		test = y
	print ''.join(map(str, my_counts))

	print test

def getPermutations(string):
    if len(string) == 1:
        yield string
    else:
        for i in xrange(len(string)):
            for perm in getPermutations(string[:i] + string[i+1:]):
                yield string[i] + perm

if __name__ == "__main__":
	# for i in getPermutations('012'):
	# 	print i
	# print map(str,lexi(list([0,1,2,3,4,5,6,7,8,9])))

	print [sum for i in (lexi(list([0,1,2,3,4,5,6,7,8,9])))]
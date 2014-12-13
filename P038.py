digits = set([1,2,3,4,5,6,7,8,9])


def is_pandigit(test_num):
	pand_check = False
	if len(str(test_num))==9:
		test_list = [int(x) for x in str(test_num)]
		test_set = set(test_list)
		if test_set == digits:
			pand_check= True
	return	pand_check


def problem():
	for n in xrange(2,100):
		int_list = range(1,n+1)

		for x in xrange(10000,1,-1):

			test_sum = list(str(x * y) for y in int_list)

			if is_pandigit(''.join(test_sum)):
				print n,x,test_sum
				break



if __name__ == "__main__":
	print problem()
	print is_pandigit(198273645)
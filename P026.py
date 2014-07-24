def recur_fract(x):
	pattern = ''
	divisor = x
	top_num = 1000
	for i in xrange(10000):
		a,b =  divmod(top_num, x)
		if b == 0:
			pattern += str(a)
			return False
		else:
			pattern += str(a)
			digits = len(pattern)
			for d in range(1, digits/2+1):
				if pattern[digits-2*d:digits-d] ==	pattern[digits-d:]:
						return pattern[digits-d:]
			top_num = b * 10

	return 1000
def problem():
		local_max = 0
		max_recurrance = 0
		max_item = 0

		for item in range(983,984):
			recurrance = recur_fract(item)
			if recurrance:
				if len(recurrance) > local_max:
					local_max = len(recurrance)
					max_recurrance = recurrance
					max_item = item

		print '{} is the largest item with recurrance {} = {} digits'.format(max_item,local_max,max_recurrance)


		return max_item

if __name__ == "__main__":
	# problem()
	# my_out=False
	# pattern = ''
	# divisor = 983
	# top_num = 1000
	# for i in xrange(10000):
	# 	a,b =  divmod(top_num, divisor)
	# 	# if b == 0:
	# 	# 	pattern += str(a)
	# 	# 	print False
	# 	# 	break
	# 	# else:
	# 	pattern += str(a)
	# 	digits = len(pattern)
	# 	for d in range(1, digits/2+1):
	# 		if pattern[digits-2*d:digits-d] ==	pattern[digits-d:]:
	# 				print pattern[digits-d:]
	# 				print pattern
	# 				my_out = True
	# 	if my_out:
	# 		break
	# 	top_num = b * 10
	print 1000000000000000000 / 983

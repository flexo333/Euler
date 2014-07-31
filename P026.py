def recur_fract(x):
	pattern = ''
	divisor = x
	top_num = 10
	div = [[],[],[]]
	for i in xrange(1,999): #Could use while True
		
		d,r =  divmod(top_num, x) 
		if not r in div[2]:
			div[0].append(i)
			div[1].append(d)
			div[2].append(r) 
		else:
			if div[2][-1]==0:
				return None
			else:
				return div
		# pattern += str(a)
		# if not b in div:
		# 	div.add(b)
		# else:
		# 	return len(div)

		# for d in range(1, digits/2+1):
		# 	if pattern[digits-2*d:digits-d] ==	pattern[digits-d:]:
		# 			return pattern[digits-d:]
		top_num = div[2][i-1] * 10


def problem():
		local_max = 0
		max_recurrance = 0
		max_item = 0

		for item in range(3,1000):
			recurrance = recur_fract(item)
			# print recurrance
			if recurrance:
				if recurrance[0][-1] > max_recurrance:

					max_recurrance = recurrance[0][-1]
					max_item = item

		
		# print '{} is the largest item with recurrance {}'.format(max_item,max_recurrance)

		return max_item

if __name__ == "__main__":
	problem()

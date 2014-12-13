
def problem():
	my_array =  list(list(0 for i in xrange(20)) + [1] for x in xrange(20))
	my_array += [list(1 for i in xrange(21))]
	
	for y in xrange(19,-1,-1):
		for x in xrange(19,-1,-1):
			my_array[x][y] = my_array[x+1][y] + my_array[x][y+1]


	return my_array[0][0]

if __name__ == "__main__":
	print problem()

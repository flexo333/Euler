def problem():

	infile = './P013.data.file'
	ma = list(0 for x in xrange(50))
	
	with open(infile, 'r')  as f:
		for row in f:
			row_array =  map(int,list(row[:50]))
			# a.append(row_array)
			# print row_array
			ma = [x + y for x, y in zip(ma, row_array)]

	answer = 0
	for digit in ma:
		answer = answer*10 + digit
		if len(str(answer))>15: break
	return str(answer)[:10]
		# lst = map(int, open(infile).readlines())
	# print lst

if __name__ == "__main__":
	print problem()

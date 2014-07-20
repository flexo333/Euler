def problem():
	infile = './P018.data'
	ma =[]
	with open(infile, 'r')  as f:
		for row in f:
			row_array =  map(int, row.strip().split(' '))
			ma.append(row_array)

	ma_sum = ma
	for row in xrange(len(ma)-2, -1, -1):
		for col in xrange(len(ma[row])):
			ma_sum[row][col] += max(ma[row+1][col], ma[row+1][col+1])
	return ma_sum[0][0]


if __name__ == "__main__":
	problem()
	
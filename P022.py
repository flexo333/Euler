def problem():
	infile = './P022.data'
	ma =[]
	with open(infile, 'r')  as f:
		for row in f:
			ma =  row[1:-1].split('","')
			
	ma.sort()

	return sum ( (x+ 1) * sum(ord(p.lower()) - 96 for p in y) for x,y in enumerate(ma))



if __name__ == "__main__":
	print problem()
	
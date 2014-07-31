

def problem():
	sumsq = 1
	for levels in range(3, 1003, 2):
		start = (levels-2)**2

		sumsq += (start * 4 + 10* (levels-1))
	return sumsq

if __name__ == "__main__":
	print problem()
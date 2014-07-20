def problem():
	sum_num = 0
	sum_sqnum = 0
	for y in xrange(1,101):
		sum_sqnum += y**2
		sum_num += y

	return sum_num**2-sum_sqnum

if __name__ == "__main__":
	# Load_MREPOS()
	problem()
	
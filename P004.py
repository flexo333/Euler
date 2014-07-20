
def problem():
	maxresults = 0
	for x in xrange(100,999):
		for y in xrange(100,999):
			results = x * y
			if results > maxresults:
				if int(str(results)[::-1]) == results:
					maxresults = results
					pair = [x,y]

	print maxresults
	print pair

if __name__ == "__main__":
	# Load_MREPOS()
	problem()

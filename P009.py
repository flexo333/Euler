# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
sum_int = 1000
class Found(Exception): pass

def problem():
	#First Attempt Using Nested Loops
	try:
		for x in range(1, 1001):
			for y in range(1, 1001):
				z = sum_int - x -y
				if z < 0:
					next
				if z**2 == (x**2+y**2):
					raise Found
	except Found:
		# print str(x) + ' '  + str(y) + ' '   + str(z)
		return x*y*z 

def problem_alt():
	#Second Attempt using nested Tuples.
	# for x, y in [(x,y) for x in xrange(1, 1001) for y in xrange(1, 1001)]:
	for x in range(1, 1001):
	 for y in range(1, 1001):
		z = sum_int - x -y
		if z < 0:
			next
		if z**2 == (x**2+y**2):
			break
	print(x*y*z) 



if __name__ == "__main__":
	# Load_MREPOS()
	problem()

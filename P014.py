# Longest Collatz sequence
# Problem 14
# Published on 05 April 2002 at 06:00 pm [Server Time]
# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


def series_function(number):
			if number%2==0:
				return number / 2
			else:
				return 3 * number+1


def problem():
	calculated = list(0 for x in xrange(1000000))
	
	for item in xrange(1,1000000):
		x = item
		chain = 1
		while (not x == 1) and x >= item:
			chain +=1
			x = series_function(x)
			
		if not x == 1: chain += calculated[x-1]-1
		calculated[item-1]=chain

	 
	return calculated.index(max(calculated))+1


if __name__ == "__main__":
	print problem()

from eulertools import isprime

def my_function(n,a,b):
	result = n**2 + a * n + b
	return result


def problem():
	maxn = 38

	for a in xrange(-1000, 1000):
			for b in xrange(-1000, 1000):
				n = 0

				while isprime(my_function(n, a, b)):
					n += 1
				if n > maxn:
					maxn = n
					answer = [a,b,n-1]
	return answer[0] * answer[1]


if __name__ == "__main__":
	print problem()
import eulertools as et

def my_function(n,a,b):
	result = n**2 + a * n + b
	return result

def problem():
	maxn = 0
	for a in range(-1000, 1000):
			for b in range(-1000, 1000):
				n = 0

				while et.isprime(my_function(n, a, b)):
					n += 1
				if n > maxn:
					maxn = n
					answer = [a,b,n-1]

	return answer[0] * answer[1]


def problem_wsimon():
	maxn = 0
	P =set(et.primeseive(10000))
	for a in range(-1000, 1000):
			for b in range(-1000, 1000):
				n = 0

				while n**2 + a * n + b in P:
					n += 1
				if n > maxn:
					maxn = n
					answer = a * b

	return answer

if __name__ == "__main__":
	print(problem())




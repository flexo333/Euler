import eulertools

def problem():
	primelist = eulertools.primeseive(800000)
	primelist = set(primelist)
	trunct_list = []
	start = 10
	print("Start")
	for i  in primelist:
		prime_i = True
		if i < 10:
			prime_i = False
		# print 'Prime',i
		for x in range(1,len(str(i))):
			# print x,int(str(i)[x:]),int(str(i)[:-x])
			# print int(str(i)[:-x]) in primelist
			if not int(str(i)[x:]) in primelist:
				prime_i = False
				break
			if not int(str(i)[:-x]) in primelist:
				prime_i = False
				break
		if prime_i == True:
			trunct_list += [i]

	return sum(trunct_list)

if __name__ == "__main__":
	print(problem())
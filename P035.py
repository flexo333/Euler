import eulertools


def problem():
	primelist = eulertools.primeseive(1000000)
	primelist_set = set(primelist)
	cp_list = []
	for i in primelist:
	# for i in [197,198,971]:
		cp = True
		for x in range(1,len(str(i))):
			if not int(str(i)[x:] + str(i)[:x]) in primelist_set:
				cp = False
			# if int(str(i)[x:] + str(i)[:x]) in cp_list:
			# 	cp = False
		if cp == True:
			cp_list += [i]
	return len(cp_list)



if __name__ == "__main__":
	print(problem())
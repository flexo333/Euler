def lexi(number_l):
	number_list = number_l
	if len(number_list)<=1:
		yield str(number_list[0])
	else:
		for x in number_list:
			for y in lexi([i for i in number_list if i != x]):
				yield str(x) + str(y)
				
def fact(n):
	prod = 1
	for x in range(1,n+1):
		prod *= x
	return prod

def problem():
	# for i in xrange(p):
	my_list = [fact(i) for i in range(9,0,-1)]
	test = 10**6

	my_counts = []
	for item in my_list:
		x,y = divmod(test,item)
		if y == 0:
			my_counts.append(max([x-1,0]))
		else:
			my_counts.append(x)
		test = y
	num_list = list(range(0,10))
	
	answer=''
	for item in my_counts:
		if item ==0:
			answer += str(num_list.pop(-1))
		else:
			answer += str(num_list.pop(item))
	answer += str(num_list.pop(0))
	return answer

def getPermutations(string):
    if len(string) == 1:
        yield string
    else:
        for i in range(len(string)):
            for perm in getPermutations(string[:i] + string[i+1:]):
                yield string[i] + perm

def brute_force():
	counter = 0
	for i in (lexi(list([0,1,2,3,4,5,6,7,8,9]))):
		counter += 1
		if counter == 1000000:
			print(i)
			break


if __name__ == "__main__":

	# brute_force()
	print(problem())
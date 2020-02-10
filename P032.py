pd = (1,2,3,4,5,6,7,8,9)

def lexi(number_l):
	number_list = number_l
	if len(number_list)<=1:
		yield str(number_list[0])
	else:
		for x in number_list:
			for y in lexi([i for i in number_list if i != x]):
				yield str(x) + str(y)

def problem():
	threesets = []
	for a in range(1,5):
		for b in range(1,5):
			c = 9 - a - b
			if not sorted([a, b, c]) in threesets and max(a,b,c) < 5:
				threesets += [sorted([a, b, c])]
	newsets = threesets
	matches = []

	for r in lexi(pd):
		for i in newsets:
			x,y,z = int(r[:i[0]]), int(r[i[0]:i[0]+i[1]]) , int(r[i[0]+i[1]:])
			if x * y ==z :
				matches += [z]
			if x * z == y:
				matches += [y]
			if z * y ==x :
				matches += [x]

	products = []
	products = set(matches)
	return sum(products)

if __name__ == "__main__":
	print(problem())	
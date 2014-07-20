def lexi(number_l):
	number_list = number_l


	if len(number_list)<=1:
		yield str(number_list[0])
	else:
		for x in number_list:
			for y in lexi(number_list[:-len(number_list)+1]):
				yield str(x) + str(y)
				


def problem():
	# print map(int,lexi(list([3,5,8,9])))
	for item in lexi([3,5,8,9]):
		print item

if __name__ == "__main__":
	problem()

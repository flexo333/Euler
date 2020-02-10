
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2*1000?

def problem():
	num =  2**1000
	str_num = str(num)
	list_num = list(map(int, list(str_num)))
	return sum(list_num)



if __name__ == "__main__":
	print(problem())

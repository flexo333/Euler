def sum5power(n):
	sum_return = 0
	for i in str(n):
		sum_return += int(i)**5
	return sum_return

def problem():
 	list_p5 = []
 	for x in range(2,5 * 9**5):
 		if sum5power(x) == x:
 			list_p5.append(x)
 	sumnn = 0
 	for item in list_p5:
 		sumnn += item 
 	return sumnn
 	
if __name__ == "__main__":
	print problem()
	 
def palindrome_check(my_num):
	if str(my_num)[::-1] == str(my_num):
		return True
	else:
		return False

def palindrome_seive(max_n):
	numbers = range(1, max_n+1)

	for i in range(1, max_n+1):
		if not palindrome_check(i):
			numbers[i-1] = 0

	return filter(None, numbers)

def problem():
	palindrome_list = palindrome_seive(1000000)
	binary_palindrome = []
	for item in palindrome_list:
		if palindrome_check(bin(item)[2:]):
			binary_palindrome += [item]

	return sum(binary_palindrome)

if __name__ == "__main__":
	print problem()
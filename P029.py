

def problem():
	whole_list = []
	for a in range(2, 101):
		for b in range(2, 101):
			whole_list.append(a**b)
	short_list = set(whole_list)
	return len(short_list)

if __name__ == "__main__":
	print(problem())
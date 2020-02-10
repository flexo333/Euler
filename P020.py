def problem():
	prod =1
	for x in range(1, 101, 1):
		prod *=x
	return sum(map(int,list(str(prod))))



if __name__ == "__main__":
	print(problem())

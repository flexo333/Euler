def problem():
	largest_p = 0
	longest_p = 0
	for p in range(3,1000):
		# print p
		x = 1
		y = 1
		tri_list = []
		for x in range(1, p-1):
			for y in range(x,p-x):
				z = p - x - y
				tri_num = (x,y,z)
				t = sorted(tri_num)
				if t[0]**2 + t[1]**2 == t[2]**2:
					tri_list += [t]
	
		# k = sorted(tri_list)
		# dedup = [k[i] for i in range(len(k)) if i == 0 or k[i] != k[i-1]]
		
		if len(tri_list)>longest_p:
			largest_p = p
			longest_p = len(tri_list)

	print largest_p





if __name__ == "__main__":
	print problem()
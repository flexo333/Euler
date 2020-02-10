month_dict = {1:31, 2:28,3:31,4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31,11:30,12:31}

def month_add(m,y):
	if m==2 and y%4==0 and (not y%100==0 or y%400==0):
		return 29
	else:
		return month_dict[m]


def problem():
	day_count = -2
	for year in range(1900,1901,1):
		for item in month_dict:
			day_count += month_add(item,year)
	monday_counter = 0

	for year in range(1901,2001,1):
		for item in month_dict:
			if (day_count + 1)%7==0:
				monday_counter+=1
			day_count += month_add(item,year)
	return monday_counter


if __name__ == "__main__":
	print(problem())
	
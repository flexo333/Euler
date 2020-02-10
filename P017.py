single_dict = {0:'', 1:'one', 2:'two',3:'three',4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
tens_dict = {0:'',1:'', 2:'twenty',3:'thirty',4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
teens_dict = {0:'ten',1:'eleven', 2:'twelve',3:'thirteen',4:'fourteen', 5:'fifteen', 6:'sixteen', 7:'seventeen', 8:'eighteen', 9:'nineteen'}

def num_to_word(x):
	wordnum=''
	num_list = list(map(int, list(str(x).zfill(3))))
	wordnum += single_dict[num_list[0]]
	if not num_list[0] == 0:
		wordnum += 'hundred'
		if not (num_list[1] + num_list[2]) == 0: wordnum += 'and'
	if num_list[1]==1:
		wordnum += teens_dict[num_list[2]]
	else:
		wordnum += tens_dict[num_list[1]]
		wordnum += single_dict[num_list[2]]
	return wordnum



def problem():
	counter = 0
	for i in range(1,1001):
		# print num_to_word(i)
		counter += len(num_to_word(i))
	return counter + 1


if __name__ == "__main__":
	print(problem())

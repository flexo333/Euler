d = { chr(ord('A')+x) : x+1 for x in range(26) }
def triangle(n):
	tri_n = 0.5 * n * (n + 1)
	return tri_n
def tri_word(Test_word):
	word_value = 0
	for l in Test_word:
		word_value += d[l]
	return word_value
	
def problem():

	tri_l = [triangle(x) for x in range(1,500)]

	tri_l = set(tri_l)
	infile = './P042_words.txt'
	wordslist =[]
	with open(infile, 'r')  as f:
		for row in f:
			wordslist = row.replace('"', "").split(',')
	n = 0

	for item in wordslist:
		tri_value = tri_word(item)
		if tri_value in tri_l:
			n += 1
	return n

if __name__ == "__main__":
	print(problem())
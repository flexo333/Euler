def fibonacci(x):
	"""Returns the xth number in the Fibonacci sequence"""
	fa = 1
	fb = 1
	if x > 0:
		yield fa
	if x > 1:	
		yield fb
	if x > 2:
		for item in xrange(3,x+1):
			interim=fa+fb
			fa=fb
			fb = interim
			yield fb

def problem():
	for x,item in enumerate(fibonacci(5000)):
		if len(str(item))>999:
			return x+1
			break
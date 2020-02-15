
from eulertools import is_prime, lexi
	

def problem():

	for i in lexi([9,8,7,6,5,4,3,2,1]):
	    if is_prime(float(i)):
	        return i

	for i in lexi([8,7,6,5,4,3,2,1]):
	    if is_prime(float(i)):
	        return i


	for i in lexi([7,6,5,4,3,2,1]):
	    if is_prime(float(i)):
	        return i
	        break






if __name__ == "__main__":
	print(problem())
def problem():
	products = 1.0
	for d in range(10,100):
		for n in range(10, d):
	# 		d= int(d)
	# 		n= int(n)
	# 		if not (d % 10 == 0):
	# 			if not (n % 10 == 0):
			
	# 				d = str(d)
	# 				n = str(n)
	# 				if float(n)/float(d) in [float(n[0])/float(d[0]),float(n[0])/float(d[1]),float(n[1])/float(d[0]),float(n[1])/float(d[1])]:
	# 					print n, '/', d
	# 					products *= float(n)/float(d)
	# return products

			if not (d % 10 == 0):
				if not (n % 10 == 0):
					d1,d2 = float(str(d)[0]),float(str(d)[1])
					n1,n2 = float(str(n)[0]),float(str(n)[1])
					d = float(d)
					n = float(n)
					# print d1,d2,n1,n2,d,n

					if d1==n1 and n2/d2 == n/d:
						products *= n/d
						# print d1,d2,n1,n2,d,n
					if d1==n2 and n1/d2 == n/d:
						products *= n/d
						# print d1,d2,n1,n2,d,n
					if d2==n1 and n2/d1 == n/d:
						products *= n/d
						# print d1,d2,n1,n2,d,n
					if d2==n2 and n1/d1 == n/d:
						products *= n/d
						# print d1,d2,n1,n2,d,n

	answe = 1/products
	return int(answe)+1


if __name__ == "__main__":
	print problem()
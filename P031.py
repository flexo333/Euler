def coin_return(coins, my_value):
	if len(coins)==1:
		yield [(coins[0], my_value/coins[0])]
	elif my_value == 0:
		zeroes = []
		for item in coins:
			zeroes.append((item,0))
		yield zeroes
		# yield None
	else:
		for x,coin in enumerate(coins):
			for i in range(1,my_value/coin+1):
				for j in coin_return(coins[x+1:],max(my_value - i*coin,0)):
					yield [(coin, i)],j

def problem():
	coins = [200,100,50,20,10,5,2,1]
	my_value = 200
	counter = 0
	for item in coin_return(coins, my_value):
		counter += 1
	return counter

 	
if __name__ == "__main__":
	print(problem())	
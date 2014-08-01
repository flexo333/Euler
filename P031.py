

def problem(coins, my_value):
	for x,coin in enumerate(coins):
		for i in range(1,200/coin+1):
			problem(coins[x+1:],my_value - i*coin)


 	
if __name__ == "__main__":
	coins = {200,100} #,50,20,10,5,2,1}
	my_value = 200
	print problem(coins, my_value)
	 
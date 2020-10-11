# Similar to 0-1 knapsack we have choice diagram
# however if we reject an item -> processed
# if we select an item -> not processed, call over it again
# hence just change function call

# weight array
wt = [1, 2, 5, 3]
# value array
val = [40, 30, 50, 20]
# capacity of knapsack
W = 2
# number of items
N = len(val)

def unboundedKnapsack (wt, val, W, N):
	# dp tabular array
	# if array size is 0 -> profit always zeo
	# if knapsack capacity is 0 -> profit always zero
	K =[[0 for x in range(W+1)] for y in range (N+1)]

	for i in range (1, N+1):
		for j in range (1, W+1):
			if wt[i-1] > j:
				K[i][j] = K[i-1][j]
			elif wt[i-1] <= j:
				# here if an item is selected it is possible that it can be selected again (unbounded)
				# therefore i (index) will not change
				K[i][j] =  max(K[i-1][j], val[i-1]+K[i][j-wt[i-1]])
	
	return K[N][W]

if __name__ == '__main__':
	profit = unboundedKnapsack(wt, val, W, N)
	print(profit)

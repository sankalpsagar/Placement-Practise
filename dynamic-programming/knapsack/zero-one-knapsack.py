# Weight Array
wt = [8, 16, 32, 40]
# Value Array
val = [50, 100, 150, 200]
# Capacity
W = 64
# Total number of items
N = len(val)

def knapsack (wt, val, W, n):
	if W==0 or n==0:
		# Base condition
		return 0

	if wt[n-1] > W:
		# not possible to add it
		return knapsack(wt, val, W, n-1)

	else:
		# check if adding will introduce max or not
		return max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))

if __name__ == '__main__':
	profit = knapsack(wt, val, W, N)
	print(profit)
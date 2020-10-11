# Weight Array
wt = [8, 16, 32, 40]
# Value Array
val = [50, 100, 150, 200]
# Capacity
W = 64
# Total number of items
N = len(val)

# DP matrix
t = [[-1 for x in range(W+1)] for y in range(N+1)]

def knapsack (wt, val, W, n):
	if W==0 or n==0:
		# Base condition
		return 0

	if t[N][W] != -1:
		return t[N][W]

	if wt[n-1] > W:
		# not possible to add it
		t[N][W] = knapsack(wt, val, W, n-1)
		return t[N][W]

	else:
		# check if adding will introduce max or not
		t[N][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
		return t[N][W]

if __name__ == '__main__':
	profit = knapsack(wt, val, W, N)
	print(profit)
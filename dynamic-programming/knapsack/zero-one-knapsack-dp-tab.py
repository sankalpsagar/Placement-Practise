# Weight Array
wt = [8, 16, 32, 40]
# Value Array
val = [50, 100, 150, 200]
# Capacity
W = 64
# Total number of items
N = len(val)

# DP tabular matrix
K = [[0 for x in range(W+1)] for y in range(N+1)]

def knapsack (wt, val, W, N):
	for i in range (N+1):
		for j in range (W+1):
			if i==0 or j==0:
				K[i][j] = 0
			elif wt[i-1] <= j:
				K[i][j] = max(val[i-1]+K[i-1][j-wt[i-1]], K[i-1][j])
			else:
				K[i][j] = K[i-1][j]	

	return K[N][W]


if __name__ == '__main__':
	profit = knapsack(wt, val, W, N)
	print(profit)
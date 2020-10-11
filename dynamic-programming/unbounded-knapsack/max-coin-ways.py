# same as unbounded since you have infinite supply of coins
coins = [1, 2, 3]
targetsum = 4
n = len(coins)

def maxCoinWays (coins, targetsum, n):
	K = [[0 for x in range(targetsum+1)] for y in range(n+1)]

	# initialization, if sum=0 and coins=0, no of ways is 1 (phi set)
	# otherwise if sum=0 and coins=1-2-3, no of ways is again 1 (phi set)

	for i in range(n+1):
		K[i][0] = 1

	for i in range (1, n+1):
		for j in range (1, targetsum+1):
			if coins[i-1] > j:
				K[i][j] = K[i-1][j]
			elif coins[i-1] <= j:
				# unbounded so index remains unchanged
				K[i][j] = K[i-1][j] + K[i][j-coins[i-1]]

	return K[n][targetsum]

if __name__ == '__main__':
	ways = maxCoinWays(coins, targetsum, n)
	print(ways)
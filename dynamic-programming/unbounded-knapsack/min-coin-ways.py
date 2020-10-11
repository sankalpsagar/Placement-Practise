# to find min no of coin changes required

# to use an infinite value
import sys
coins = [1,2,3]
targetsum = 4
n = len(coins)

def minCoinWays(coins, targetsum, n):
	K = [[0 for x in range(targetsum+1)] for y in range (n+1)]

	# here if coins = 0 and sum = 1, 2, 3, etc then no of coins required will be infinity

	for i in range (targetsum+1):
		K[0][i] = sys.maxsize - 1

	for i in range (1, n+1):
		for j in range (1, targetsum+1):
			if coins[i-1] > j:
				K[i][j] = K[i-1][j]
			elif coins[i-1] <= j:
				K[i][j] = min( K[i-1][j], 1 + K[i][j-coins[i-1]])

	return K[n][targetsum]

if __name__ == '__main__':
	ways = minCoinWays(coins, targetsum, n)
	print(ways)
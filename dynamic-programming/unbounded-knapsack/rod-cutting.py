# literally the same problem as unbounded knapsack
# except a few minor stuff

# length of pieces
length = [2, 4, 6, 8]
# price array
price = [20, 40, 45, 50]
# length of rod
L = 8
# number of pieces
N = len(price)

def rodCutting(length, price, L, N):
	# if rod length is 0, no profit
	# if size of piece is 0 no profit
	K = [[0 for x in range(L + 1)] for y in range (N+1)]

	for i in range (N+1):
		for j in range (L+1):
			if length[i-1] > j:
				K[i][j] = K[i-1][j]
			elif length[i-1] <= j:
				K[i][j] = max(K[i-1][j], price[i-1]+K[i][j-length[i-1]])

	return K[N][L]

if __name__ == '__main__':
	profit = rodCutting(length, price, L, N)
	print(profit)

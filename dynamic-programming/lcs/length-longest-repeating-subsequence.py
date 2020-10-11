X = "aab"
m = len(X)

def LRSS (X, m):
	Y = X[:]
	# print(Y)
	n = len(Y)
	K = [[0 for x in range(n+1)] for y in range (n+1)]

	for i in range (1, n+1):
		for j in range (1, m+1):
			if X[i-1] == Y[j-1] and i!=j:
				K[i][j] = 1 + K[i-1][j-1]
			else:
				K[i][j] = max (K[i-1][j], K[i][j-1])

	return K[m][m]

if __name__ == '__main__':
	count = LRSS(X, m)
	print(count)
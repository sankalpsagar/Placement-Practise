# shortest common superstring
X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)

def scs (X, Y, m, n):
	K = [[0 for x in range(n+1)] for y in range (m+1)]

	for i in range (1, m+1):
		for j in range (1, n+1):
			if X[i-1] == Y[j-1]:
				K[i][j] = 1 + K[i-1][j-1]
			elif X[i-1] != Y[j-1]:
				K[i][j] = max (K[i-1][j], K[i][j-1])

	length = K[m][n]

	# now we know what letters are common
	# we subtract them from total length to get shortest common superstring

	return m+n-length

if __name__ == '__main__':
  	length = scs (X, Y, m, n)
  	print(length)  
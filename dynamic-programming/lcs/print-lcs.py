# Largest common subsequence
X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)

def lcs (X, Y, m, n):
	K = [[0 for x in range(n+1)] for y in range (m+1)]

	for i in range (1, m+1):
		for j in range (1, n+1):
			if X[i-1] == Y[j-1]:
				K[i][j] = 1 + K[i-1][j-1]
			elif X[i-1] != Y[j-1]:
				K[i][j] = max (K[i-1][j], K[i][j-1])

	i = m
	j = n
	index = K[m][n]

	res = [""]*(index+1)
	res[index] = ""

	while i>0 and j>0:
		if X[i-1] == Y[j-1]:
			res[index] = X[i-1]			
			i -= 1
			j -= 1
			index -= 1
		else:
			if K[i-1][j] > K[i][j-1]:
				i -= 1
			else:
				j -= 1

	return "".join(res)

if __name__ == '__main__':
  	length = lcs (X, Y, m, n)
  	print(length)  
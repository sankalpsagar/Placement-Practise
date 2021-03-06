# AXY is present in ADXCPY
# so pattern matched

X = "AXY"
Y = "ADXCPY"
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

	return K[m][n]

def patternMatching(X, Y, m, n):
	count = lcs(X, Y, m, n)
	if (count == m):
		return True
	else:
		return False

if __name__ == '__main__':
  	length = patternMatching (X, Y, m, n)
  	print(length)  
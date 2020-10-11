# Largest common substring
X = "abcdxyz"
Y = "xyzabcd"
m = len(X)
n = len(Y)

def lcSubstring(X, Y, m, n):
	K = [[0 for x in range(n+1)] for y in range (m+1)]

	maxcount = -99999

	for i in range(1, m+1):
		for j in range(1, n+1):
			if X[i-1] == Y[j-1]:
				K[i][j] = K[i-1][j-1] + 1
				maxcount = max (maxcount, K[i][j])
			else:
				K[i][j] = 0

	return maxcount

if __name__ == '__main__':
  	length = lcSubstring (X, Y, m, n)
  	print(length)  
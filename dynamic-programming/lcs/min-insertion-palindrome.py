# LPS = LCS(string, rev(string))
# no of insertions = no of deletions required

X = "abcgba"
n = len(X)

def LCS(X, Y, m, n):
	K = [[0 for x in range(n+1)] for y in range (m+1)]
	# Anytime a string len is 0, lcs is automatically 0

	for i in range (1, m+1):
		for j in range (1, n+1):
			if X[i-1] == Y[j-1]:
				K[i][j] = 1 + K[i-1][j-1]
			else:
				K[i][j] = max (K[i-1][j], K[i][j-1])

	return K[m][n]

def LPS(X, n):
	Y = X[::-1]
	# print(Y)
	length = LCS (X, Y, n, len(Y))
	return length

if __name__ == '__main__':
	length = LPS(X, n)
	print(length)
	print("Min no of insertions required: ", str(n-length))
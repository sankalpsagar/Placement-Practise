# min ins or del required to change string a to string b
X = "heap"
Y = "pea"
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

def minInsOrDel(X, Y, m, n):
	lcsres = lcs(X, Y, m, n)
	# print(lcsres)
	deletion = m - lcsres
	insertion = n - lcsres
	return deletion, insertion

if __name__ == '__main__':
  	dele, ins = minInsOrDel (X, Y, m, n)
  	print("String a:", X, "String b:", Y)
  	print("Deleted: ", dele, " Inserted: ", ins)  
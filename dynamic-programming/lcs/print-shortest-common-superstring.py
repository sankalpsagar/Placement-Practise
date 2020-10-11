X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)

def SCS(X, Y, m, n):
	K = [[0 for x in range(n+1)] for y in range (m+1)]

	for i in range (1, m+1):
		for j in range (1, n+1):
			if X[i-1] == Y[j-1]:
				K[i][j] = 1 + K[i-1][j-1]
			elif X[i-1] != Y[j-1]:
				K[i][j] = max (K[i-1][j], K[i][j-1])

	print("Length of shortest common superstring is", str(m+n-K[m][n]))

	i = m
	j = n
	index = m+n-K[m][n] 
	res = [""]*(index+1)
	res[index] = ""


	while i>0 and j>0:
		if X[i-1] == Y[j-1]:
			res[index] = X[i-1]
			index -= 1
			i -= 1
			j -= 1

		else:
			if K[i-1][j] > K[i][j-1]:
				res[index] = X[i-1]
				index -= 1
				i-=1
			else:
				res[index] = Y[j-1]
				index -= 1
				j-=1

	while i>0:
		res[index] = X[i-1]
		index -= 1
		i -= 1

	while j>0:
		res[index] = Y[j-1]
		index -= 1
		j -= 1
	return "".join(res)

if __name__ == '__main__':
	string = SCS(X, Y, m, n)
	print(string)
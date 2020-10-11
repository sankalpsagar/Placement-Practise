# mcm function prototype
# i, j, k
# i near left end, k in between, j near right end
# here arr = [a, b, c, d]
# where a,b = dim(matrix 1)
# b,c = dim(matrix 2)
# and so on
# therefore, for matrix i = arr[i-1], arr[i]
# to make it valid, i must start from 1
# similarly j from n-1 to include last dim as well as 2nd last
# k must go from i to j
# f(i, k) + f(k+1, j)
# could have also been f(i, k-1) to f(k, j), your choice
# take sum of two temp ans and then we need to find cost of multiplying the two
# it will be a[i-1]*a[k]*a[j] (first dim * common dim * last dim)

import sys

arr = [1, 2, 3, 4, 3]
n = len(arr)

# memoized array
t = [[-1 for x in range(n)] for j in range (n)]

def mcm(arr, i, j):

	# array is of dimension 1 or less
	if i==j:
		return 0

	if t[i][j] != -1:
		return t[i][j]

	minans = sys.maxsize

	for k in range (i, j):

		tempans = (mcm(arr, i, k) + mcm(arr, k+1, j) + arr[i-1]*arr[k]*arr[j])

		if tempans < minans:
			minans = tempans

	t[i][j] = minans		
	return minans

if __name__ == '__main__':
	i = 1
	j = len(arr) - 1

	cost = mcm(arr, i, j)
	print(cost)
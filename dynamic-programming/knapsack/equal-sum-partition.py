# this is actually just an extension of subset sum 
# this in fact includes it

# the array
arr = [1, 5, 11, 5]
# length of array
n = len(arr)

def equalSumP(arr, n):
	sumarr = 0
	for i in range(n):
		sumarr += arr[i]

	# if the sum of elements is not even, there is no way we can equally partition it
	if (sumarr %2 != 0):
		return False

	else:
		return subsetSum(arr, sumarr//2, n)

def subsetSum(arr, sumarr, n):
	# same as previous
	# dp tabular array
	K = [[False for x in range(sumarr+1)] for y in range(n+1)]

	for i in range(n+1):
		K[i][0] = True

	for i in range (1, n+1):
		for j in range (1, sumarr+1):
			if arr[i-1] <= j:
				K[i][j] = K[i-1][j-arr[i-1]] or K[i-1][j]
			else:
				K[i][j] = K[i-1][j]

	return K[n][sumarr]

if __name__ == '__main__':
	condition = equalSumP(arr, n)
	print(condition)
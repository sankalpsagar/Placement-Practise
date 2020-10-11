# This differs from subset sum in the sense that you have to return count of total subsets, not just possibility
# therefore we initialize an int array instead of boolean

arr = [2, 3, 5, 8, 10]
# sum of subset
sumarr = 10
n = len(arr)

def subsetSumCount(arr, sumarr, n):
	# dp array
	K = [[0 for x in range(sumarr+1)] for y in range(n+1)]
	
	# here since for j=0 sum = 0 which will be satisfied by all sets (null set)
	# no matter the length of array
	for i in range(n+1):
		K[i][0] = 1

	for i in range(1, n+1):
		for j in range (1, sumarr+1):
			if arr[i-1] > j:
				K[i][j] = K[i-1][j]
			elif arr[i-1] <= j:
				# sum all the arrays
				K[i][j] = K[i-1][j-arr[i-1]] + K[i-1][j]

	return K[n][sumarr]

if __name__ == '__main__':
	count = subsetSumCount(arr, sumarr, n)
	print(count)

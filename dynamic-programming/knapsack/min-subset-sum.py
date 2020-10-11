# In this question we have to minimize the difference in sum of two partitions of an array

#       (array)
#       /      \
#      (s1)    (range - s1)

# minimize abs|s1 - s2|
# minimize abs|s1 - range - s1|
# minimize range - 2s1 where s1 < range/2

# here range = sum of all values in array
# range: {} to {array}

array = [7, 6, 13, 1]
n = len(array)

def helperSubset(arr, arrsum, n):
	# same as subset sum
	K = [[False for x in range(arrsum+1)] for y in range (n+1)]

	for i in range(n+1):
		K[i][0] = True

	for i in range(1, n+1):
		for j in range (1, arrsum+1):
			if arr[i-1] > j:
				K[i][j] = K[i-1][j]
			elif arr[i-1] <= j:
				K[i][j] = K[i-1][j-arr[i-1]] or K[i-1][j]

	candidates = []
	for i in range(((arrsum+1)//2)):
		if K[n][i] == True:
			candidates.append(i)

	# print(candidates)
	return candidates

def minSubsetSum(arr, n):
	nrange = 0
	for num in arr:
		nrange += num

	# print(nrange)

	candidates = helperSubset(arr, nrange, n)
	
	minimum = 1000 # some infinite value
	for i in candidates:
		minimum = min(minimum, nrange-2*i)
	return minimum

if __name__ == '__main__':
	minimum = minSubsetSum(array, n)
	print(minimum)


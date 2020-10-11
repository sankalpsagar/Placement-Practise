# find partition whose difference is a given number
# sum(s1) - sum(s2) = diff
# sum(s1) + sum(s2) = sumarr
# sum(s1) = (diff+sumarr)/2
# reduced to subset sum problem

arr = [5, 6, 1, 3]
diff = 1
n = len(arr)

def countSubsetDifference(arr, diff, n):
	sumarr = 0
	for i in arr:
		sumarr += i

	s1 = ((diff+sumarr)//2)
	count = subsetSumCount(arr, s1, n)
	return count

def subsetSumCount(arr, sumarr, n):
	K = [[0 for x in range (sumarr+1)] for y in range (n+1)]

	for i in range(n+1):
		K[i][0] = 1

	for i in range(1, n+1):
		for j in range (1, sumarr+1):
			if arr[i-1] > j:
				K[i][j] = K[i-1][j]
			elif arr[i-1] <= j:
				K[i][j] = K[i-1][j-arr[i-1]] + K[i-1][j]

	return K[n][sumarr]

if __name__ == '__main__':
	count = countSubsetDifference(arr, diff, n)
	print(count)
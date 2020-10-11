# define an array 
# which is equivalent to knapsack weight array
array = [2, 3, 4, 8]
# define a sum
# which is equivalent to W (capacity)
sumarr = 11
# we only output true or false
n = len(array)

def subsetSum(arr, sumarr, n):
	# here the matrix will be defined as follows
	# for i=0 -> number of matrix elements is 0 but sum is some 0-1-2...
	# for (0,0) -> ans is True since {} has sum 0
	# for rest -> ans is false
	# for j=0 -> i.e. sum is 0, ans will always be True since {} is always a subset
	# initializing our dp tabular array
	K = [[False for x in range(sumarr+1)] for y in range(n+1)]
	
	for i in range(n+1):
		K[i][0] = True

	for i in range(1, n+1):
		for j in range(1, sumarr+1):
			if arr[i-1] <= j:
				# here max is replaced by max(True, False) which would be boolean OR
				# either select number and reduce sum by that number
				# or don't select number and reduce n
				K[i][j] = K[i-1][j-arr[i-1]] or K[i-1][j]

			if arr[i-1] > j:
				K[i][j] = K[i-1][j]
	return K[n][sumarr]

if __name__ == '__main__':
	condition = subsetSum(array, sumarr, n)
	print(condition)

# find subarray with given sum

def findS(arr, gsum):
	n = len(arr)

	i, j = 0, 0
	res = 0

	while(1):
		if (res<gsum and j<n):
			res += arr[j]
			j += 1
		elif (res>gsum and i<=j):
			res -= arr[i]
			i += 1

		else:
			break

	if (res==gsum):
		return i, j-1
	else:
		return -1

if __name__ == '__main__':
	arr = [15, 2, 4, 8, 9, 5, 10, 23] 
	gsum = 23
  
	i,j = findS(arr, gsum)
	print("Subarray found at {} and {}".format(i, j)) 
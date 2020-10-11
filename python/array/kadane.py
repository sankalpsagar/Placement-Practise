
def kadane(arr):
	n = len(arr)
	local_max = 0
	global_max = -99999999
	for i in range(n):
		local_max = max(arr[i], local_max+arr[i])
		global_max = max(global_max, local_max)
	return global_max

if __name__ == '__main__':
	print(kadane([1,2,3,-2,5]))
	print(kadane([-1, -2, -3, -4]))
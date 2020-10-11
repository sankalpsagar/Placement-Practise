def rotAr(array, D):
	N = len(array)
	if D>N:
		D = D%N

	res = array.copy()
	for i in range(N):
		res[(i - D)%N] = array[i]

	print(res)

if __name__ == '__main__':
	array = [1, 2, 3, 4, 5]
	D = 3
	rotAr(array, D)
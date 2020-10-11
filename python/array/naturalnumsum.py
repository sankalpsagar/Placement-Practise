# sum of consecutive would be a1 + a2 + a3
# N = a + a + 1 + a + 1 + 1 ....
# N = (l+1)*a + l(l+1)/2
# a = (N - L(L-1)/2)(L+1)

def nnS(n):
	count = 0
	L = 1
	while ( L*(L+1) < 2*N ):
		a = (1.0*N - (L*(L+1))/2)/(L+1)
		if (a - int(a) == 0.0):
			count += 1
		L+=1
	return count

if __name__ == '__main__':
	N = 15
	print(nnS(N))
	N = 10
	print(nnS(N))
	N = 3
	print(nnS(N))
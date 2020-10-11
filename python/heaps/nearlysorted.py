# k =  how much sorted in index
import heapq as h

def nearlyS(arr, k):
	n = len(arr)
	heap = arr[:k+1]
	h.heapify(heap)

	idx = 0

	for i in range (k+1, n):
		arr[idx] = h.heappop(heap)
		h.heappush(heap, arr[i])
		idx += 1

	while heap:
		arr[idx] = h.heappop(heap)
		idx += 1

	print(arr)

if __name__ == '__main__':
	arr = [2, 6, 3, 12, 56, 8]
	k = 3
	nearlyS(arr, k)
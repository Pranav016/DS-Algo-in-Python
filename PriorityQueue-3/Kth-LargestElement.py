import heapq


def kthLargest(lst, k): 
	minHeap = lst[:k] # Add first k elements to min heap 
	heapq.heapify(minHeap) # Add first k elements to min heap 
	n = len(lst) 
	for i in range(k,n): 
		if lst[i]>minHeap[0]: 
			heapq.heapreplace(minHeap, lst[i])
	return minHeap[0]

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)
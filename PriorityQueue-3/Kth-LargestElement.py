import heapq

# def insertHeap(heap,lst,i):
    
#     else:
#         return


def kLargest(lst, k):
    heap=lst[:k]
    heapq.heapify(heap)
    for i in range(k,n,1):
        if heap[0]<lst[i]:
            heap[0]=lst[i]
            heapq.heapify(heap)
    return heap

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans)
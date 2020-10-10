import heapq

def insertHeap(heap,lst,i):
    if heap[0]<lst[i]:
        heap[0]=lst[i]
    else:
        return


def kLargest(lst, k):
    heap=[]
    for i in range(len(lst)):
        if k>0:
            heap.append(lst[i])
            heapq.heapify(heap)
            k-=1
        else:
            insertHeap(heap,lst,i)
            heapq.heapify(heap)
    return heap

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')

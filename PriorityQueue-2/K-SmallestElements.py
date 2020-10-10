import heapq

def insertHeap(heap,lst,i):
    if heap[0]>lst[i]:
        heap[0]=lst[i]
    else:
        return



def kSmallest(lst, k):
    heap=[]
    for i in range(len(lst)):
        if k>0:
            heap.append(lst[i])
            heapq._heapify_max(heap)
            k-=1
        else:
            insertHeap(heap,lst,i)
            heapq._heapify_max(heap)
    return heap


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
for i in range(len(ans)):
    print(ans[i])

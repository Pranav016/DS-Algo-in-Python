def heapify(lst,i,n):
    parentIndex=i
    leftChild=(2*parentIndex)+1
    rightChild=(2*parentIndex)+2
    while leftChild<n:
        minIndex=parentIndex
        if lst[minIndex]>lst[leftChild]:
            minIndex=leftChild
        if rightChild<n and lst[minIndex]>lst[rightChild]:
            minIndex=rightChild
        if minIndex==parentIndex:
            return
        lst[minIndex],lst[parentIndex]=lst[parentIndex],lst[minIndex]
        parentIndex=minIndex
        leftChild=(2*parentIndex)+1
        rightChild=(2*parentIndex)+2

def heapSort(heap):
    lst=[]
    n=len(heap)
    for i in range(n//2-1,-1,-1):
        heapify(heap,i,n) # we heapify the list/array
    for i in range(n-1,-1,-1):
        heap[0],heap[i]=heap[i],heap[0] # replace the first element that is the min element with the last element of the last
        lst.append(heap.pop()) # take out the list element/ min element by popping
        heapify(heap,0,i) # then heapify again to  get the min element at the top of the list/ imaginary CBT(Complete Binary Tree) again
    return lst


# main
n=int(input())
heap=list(int(i) for i in input().split())
lst=heapSort(heap)
print(*lst)
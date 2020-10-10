# this approach has complexity O(n)


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



def heapSort(lst):
    n=len(lst)
    nonLeaf=n//2-1
    for i in range(nonLeaf,-1,-1):
        heapify(lst,i,n)
    for i in range(n-1,-1,-1):
        lst[0],lst[i]=lst[i],lst[0]
        heapify(lst,0,i)
    return 


# main
n=int(input())
lst=list(int(i) for i in input().split())
heapSort(lst)
print(*lst)
# Given an array of integers, check whether it represents max-heap or not.

# logic used- check if child nodes are larger than parent nodes

import heapq

def checkMaxHeapify(lst,i,n):
    parentIndex=i
    leftChild=(2*parentIndex)+1
    rightChild=(2*parentIndex)+2
    if leftChild<n:
        if lst[leftChild]>lst[parentIndex]:
            return False
        if rightChild<n and lst[rightChild]>lst[parentIndex]:
            return False
    return True


def checkMaxHeap(lst):
    n=len(lst)
    nonLeaf=n//2-1
    for i in range(nonLeaf,-1,-1):
        if not checkMaxHeapify(lst,i,n):
            return False
    return True

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')

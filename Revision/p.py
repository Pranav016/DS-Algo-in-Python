import heapq
import queue
from sys import stdin


def buyTicket(arr, n, k):
    t=0
    ele=arr[k]
    heapq._heapify_max(arr)
    while True:
        x=heapq._heappop_max(arr)
        if x==ele:
            t+=1
            return t
        else:
            t+=1
    


# I/O
def takeInput() :
    
    n = int(stdin.readline().strip())
    
    if n == 0 :
        return n, list(), int(stdin.readline().strip())
    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    
    k = int(stdin.readline().strip())
    
    return n, arr, k


#main
n, arr, k = takeInput()
print(buyTicket(arr, n, k))

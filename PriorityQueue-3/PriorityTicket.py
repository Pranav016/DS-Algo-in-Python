import heapq
import queue
from sys import stdin


def buyTicket(arr, n, k):
    q=queue.Queue()
    heap=[]
    time=0
    for i in range(n):
        q.put(i)
        heap.append(arr[i])
        heapq._heapify_max(heap)
    while True:
        x=q.get()
        if arr[x]==heap[0]:
            time+=1
            if k==x:
                return time
            heapq._heappop_max(heap)
        else:
            q.put(x)
    


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

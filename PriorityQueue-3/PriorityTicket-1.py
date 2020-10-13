# You want to buy a ticket for a well-known concert which is happening in your city. But the number of tickets available is limited. Hence the sponsors of the concert decided to sell tickets to customers based on some priority.
# A queue is maintained for buying the tickets and every person has attached with a priority (an integer, 1 being the lowest priority). The tickets are sold in the following manner -
# 1. The first person (pi) in the queue asked to comes out.
# 2. If there is another person present in the queue who has higher priority than pi, then ask pi to move at end of the queue without giving him the ticket.
# 3. Otherwise, give him the ticket (and don't make him stand in queue again).
# Giving a ticket to a person takes exactly 1 minutes and it takes no time for removing and adding a person to the queue. And you can assume that no new person joins the queue.
# Given a list of priorities of N persons standing in the queue and the index of your priority (indexing starts from 0). Find and return the time it will take until you get the ticket.


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

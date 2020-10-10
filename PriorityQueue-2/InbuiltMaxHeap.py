import heapq

lst=[3,8,5,4,6,9,7]

heapq._heapify_max(lst) # heapify for max heap

print(*lst)

heapq._heappop_max(lst) # max element popped and lst is re-heapified

print(*lst)

heapq._heapreplace_max(lst,0) # replace the max element of the heap

print(*lst)

# to push into a max heap- is different

lst.append(1)
heapq._siftdown_max(lst,0,len(lst)-1)  # heapq._siftdown_max(heap,startpos of heap,pos of inserted element)

print(*lst)

# also we can use heapq._siftup_max(heap,pos)
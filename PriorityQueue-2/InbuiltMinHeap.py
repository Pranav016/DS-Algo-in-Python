import heapq

lst=[3,8,5,4,6,9,7]

heapq.heapify(lst)
print(*lst)

heapq.heappush(lst,2) # to push elements to the heap

print(*lst)

print(heapq.heappop(lst)) # remove the min element

heapq.heapreplace(lst,6) # replace min element with 6 and performs heapify again
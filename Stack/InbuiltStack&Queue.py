# we can make stack from a list since list is having similar operations to implement a stack
# we can also make stack from LifoQueue, Queue is usually FIFO but a LifoQueue acts as a stack

# Stack using List

s=[1,2,3]
s.append(4)
s.append(5)

print(s.pop())
print(s.pop())

# Stack using LifoQueue

import queue

q=queue.LifoQueue()

q.put(1)
q.put(2)
q.put(3)
while not q.empty():
    print(q.get())

# to use the FIFO queue do
# q=queue.Queue()  -- FIFO queue
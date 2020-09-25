
from sys import stdin
import queue

def reverseKElements(q, k):
    if q.empty() or k<=0:
        return
    stack=[]
    while not q.empty():
        stack.append(q.get())
    l=len(stack)-k
    while stack:
        x=stack.pop()
        q.put(x)
    for i in range(l):
        stack.append(q.get())
        i+=1
    while stack:
        x=stack.pop()
        q.put(x)
    return q
    

def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty() :
    print(qu.get(), end = " ")

# we have to print nodes at depth K

import queue
from sys import stdin,setrecursionlimit

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
def levelOrderInput():
    tlist=list(map(int, stdin.readline().strip().split(" ")))
    q=queue.Queue()
    start=0
    data=tlist[start]
    if data!=-1:
        root=Node(data)
    else:
        return None
    q.put(root)
    start+=1
    while not q.empty():
        current=q.get()
        data=tlist[start]
        start+=1
        if data!=-1:
            leftChild=Node(data)
            current.left=leftChild
            q.put(leftChild)
        data=tlist[start]
        start+=1
        if data!=-1:
            rightChild=Node(data)
            current.right=rightChild
            q.put(rightChild)
    return root

def NodesAtDepthK(root,k,i):
    if root is None:
        return
    elif k==i:
        print(root.data, end=" ")
        return
    NodesAtDepthK(root.left,k,i+1)
    NodesAtDepthK(root.right,k,i+1)

# main
setrecursionlimit(10**6)
root=levelOrderInput()
k=int(input())
NodesAtDepthK(root,k,0)
        

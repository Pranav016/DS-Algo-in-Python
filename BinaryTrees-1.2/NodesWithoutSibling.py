import queue
from sys import stdin,setrecursionlimit

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    

def levelOrderInput():
    tlist=list(map(int, stdin.readline().strip().split(" ")))
    start=0
    # l=len(tlist)
    data=tlist[start]
    start+=1
    if data!=-1:
        root=Node(data)
    else:
        return None
    q=queue.Queue()
    q.put(root)
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

def NodesWithoutSiblings(root):
    if root is None:
        return
    if root.left and not root.right:
        print(root.left.data, end=" ")
    elif root.right and not root.left:
        print(root.right.data, end=" ")
    NodesWithoutSiblings(root.left)
    NodesWithoutSiblings(root.right)

# main
setrecursionlimit(10**6)
root=levelOrderInput()
NodesWithoutSiblings(root)
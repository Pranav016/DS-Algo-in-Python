import queue
from sys import stdin,setrecursionlimit

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def levelOrderInput():
    q=queue.Queue()
    tlist=list(map(int,stdin.readline().strip().split(" ")))
    start=0
    l=len(tlist)
    data=tlist[start]
    start+=1
    if data!=-1:
        root=Node(data)
    q.put(root)
    while not q.empty():
        current=q.get()
        data=tlist[start]
        start+=1
        if data!=-1:
            leftChild=Node(data)
            current.left=leftChild
            q.put(leftChild)
        if start<l:
            data=tlist[start]
            start+=1
            if data!=-1:
                rightChild=Node(data)
                current.right=rightChild
                q.put(rightChild)
    return root

def printLevelOrder(root):
    if root is None:
        return
    q=queue.Queue()
    q.put(root)
    while not q.empty():
        current=q.get()
        print(current.data,end=":")
        if current.left:
            q.put(current.left)
            print("L:{},".format(current.left.data),end="")
        else:
            print("L:-1",end=",")

        if current.right:
            q.put(current.right)
            print("R:{}".format(current.right.data),end="")
        else:
            print("R:-1",end="")
        print()
    
# main
setrecursionlimit(10**6)
root=levelOrderInput()
printLevelOrder(root)

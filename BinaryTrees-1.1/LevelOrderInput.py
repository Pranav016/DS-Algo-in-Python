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
        return 0
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

def printTreeDetailed(root):
    if root is None:
        return
    print(root.data,end=": ")
    if root.left:
        print("L", root.left.data, end=", ")
    if root.right:
        print("R", root.right.data, end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

# main
root=levelOrderInput()
printTreeDetailed(root)
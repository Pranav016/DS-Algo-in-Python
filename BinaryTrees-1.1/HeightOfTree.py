# maximum number of nodes in a tree of height h are (2^h -1) and minimum are h


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


def HeightOfTree(root):
    if root is None:
        return 0
    leftHeight=HeightOfTree(root.left)
    rightHeight=HeightOfTree(root.right)
    height=max(leftHeight,rightHeight)
    return height+1


# main
setrecursionlimit(10**6)
root=levelOrderInput()
print(HeightOfTree(root)) 
    
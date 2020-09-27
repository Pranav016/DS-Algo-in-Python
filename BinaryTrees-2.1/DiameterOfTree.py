# this solution takes O(nlogn) in best case and O(n^2) in worst case


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

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left),height(root.right))

def diameter(root):
    if root is None:
        return 0
    r=height(root.left)+height(root.right)
    ld=diameter(root.left)
    rd=diameter(root.right)
    return max(r,ld,rd)
    

# main
setrecursionlimit(10**6)
root=levelOrderInput()
print(1+diameter(root))
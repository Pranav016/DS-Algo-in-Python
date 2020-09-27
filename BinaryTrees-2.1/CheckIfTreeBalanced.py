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
    return 1 + max(height(root.left), height(root.right))

def isBalanced(root):
    if root is None:
        return True
    lh=height(root.left)
    rh=height(root.right)
    if lh-rh > 1 or rh-lh > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)

# main
setrecursionlimit(10**6)
root=levelOrderInput()
print(isBalanced(root))
# time complexity of this approach is O(n) for both best and worst case


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


def checkBalanced(root):
    if root is None:
        return 0,True
    lh,leftBalanced=checkBalanced(root.left)
    rh,rightBalanced=checkBalanced(root.right)
    h=1 + max(lh,rh)
    return h , leftBalanced and rightBalanced

# main
setrecursionlimit(10**6)
root=levelOrderInput()
print(checkBalanced(root)[1])
# if checkBalanced(root)[1]:
#     print("true")
# else:
#     print("false")
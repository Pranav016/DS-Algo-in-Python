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
    l=len(tlist)
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
        if start<l:
            data=tlist[start]
            start+=1
            if data!=-1:
                rightChild=Node(data)
                current.right=rightChild
                q.put(rightChild)
    return root


def mirrorTree(root):
    if root is None:
        return
    mirrorTree(root.left)
    mirrorTree(root.right)
    if root.left and root.right:
        temp=root.left
        root.left=root.right
        root.right=temp
        return
    else:
        return


def printLevelATNewLine(root):
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

# main
setrecursionlimit(10**6)
root=levelOrderInput()
mirrorTree(root)
printLevelATNewLine(root)
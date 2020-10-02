# Given a sorted integer array A of size n which contains all unique elements. You need to construct a balanced BST from this sorted input array. Return the root of constructed BST.


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    l=len(lst)
    if l==0:
        return None
    if l%2==0:
        mid=l//2-1
    else:
        mid=l//2
    data=lst[mid]
    leftLst=lst[:mid]
    rightLst=lst[mid+1:]
    root=BinaryTreeNode(data)
    root.left=constructBST(leftLst)
    root.right=constructBST(rightLst)
    return root

def preOrder(root):
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
root=constructBST(lst)
preOrder(root)

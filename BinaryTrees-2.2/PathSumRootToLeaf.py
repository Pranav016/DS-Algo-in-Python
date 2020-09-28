# Given a binary tree and a number k, print out all root to leaf paths where the sum of all nodes value is same as the given number k.


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rootToLeafPathsSumToK(root, k, lst):
    
    if root is None:
        return
    a=root.data
    lst.append(a)
    k=k-a
    if root.left is None and root.right is None:
        if k==0:
            for i in range(len(lst)):
                if i<len(lst)-1:
                	print(lst[i],end=" ")
                else:
                	print(lst[i])
        
        lst.pop()
        
        return
    else:
        rootToLeafPathsSumToK(root.left, k, lst)
        rootToLeafPathsSumToK(root.right, k, lst)
        
        lst.pop()
        return

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k=int(input())
rootToLeafPathsSumToK(root, k, [])

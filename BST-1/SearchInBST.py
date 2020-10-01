# best case time complexity of searching in BST is O(logn) and worst case is O(n)


import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def searchInBST(root,k):
    if root is None:
        return
    if root.data==k:
        return root
    elif root.data>k:
        return searchInBST(root.left,k)
    elif root.data<k:
        return searchInBST(root.right,k)

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


# main
levelOrder = [int(i) for i in input().strip().split()]
root=buildLevelTree(levelOrder)
k=int(input())
node=searchInBST(root,k)
if node:
    print(node.data)
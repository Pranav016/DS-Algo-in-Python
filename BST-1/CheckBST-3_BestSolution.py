import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def isBST(root,minimum,maximum): 
    if root is None:
        return True
    if root.data<minimum or root.data>maximum:
        return False
    isLeftBST=isBST(root.left,minimum,root.data-1)
    isRightBST=isBST(root.right,root.data+1,maximum)
    return isLeftBST and isRightBST

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
maximum=1000000
minimum=-1000000
print(isBST(root,minimum,maximum))
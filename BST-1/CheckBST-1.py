import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
def minimumNode(root):
    if root is None:
        return 1000000
    leftMin=minimumNode(root.left)
    rightMin=minimumNode(root.right)
    return min(root.data,leftMin, rightMin)
    return root.data

def maximumNode(root):
    if root is None:
        return -1000000
    leftMax=maximumNode(root.left)
    rightMax=maximumNode(root.right)
    return max(root.data,leftMax,rightMax)

def isBST(root):
    if root is None:
        return True
    leftMax=maximumNode(root.left)
    rightMin=minimumNode(root.right)
    if root.data<=leftMax:
        return False
    elif root.data>rightMin:
        return False
    else:
        return True
    
    leftBST=isBST(root.left)
    rightBST=isBST(root.right)
    return leftBST and rightBST


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
print(isBST(root))
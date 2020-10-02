import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def isBST(root):
    if root is None:
        return 1000000,-1000000,True
    leftMin,leftMax,isLeftBST=isBST(root.left)
    rightMin,rightMax,isRightBST=isBST(root.right)
    minimum=min(leftMin,rightMin,root.data)
    maximum=max(leftMax,rightMax,root.data)
    isTreeBST=True
    if root.data<=leftMax or root.data>rightMin:
        isTreeBST=False
    if not isLeftBST or not isRightBST:
        isTreeBST=False
    return minimum,maximum,isTreeBST


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
print(isBST(root)[2])
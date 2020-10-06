# You are given a Binary Tree of type integer, a target node, and an integer value K.
# Print the data of all nodes that have a distance K from the target node. The order in which they would be printed will not matter.


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def nodesAtDistanceKHelper(root, target, k) :
    if root is None :
        return -1
    if root.data == target :
        nodesAtDistanceKDown(root, k)
        return 0

    leftD = nodesAtDistanceKHelper(root.left, target, k)
    if leftD != -1 :
        if (leftD + 1) == k :
            print(root.data)
        else :
            nodesAtDistanceKDown(root.right, k - leftD - 2)
        return 1 + leftD

    rightD = nodesAtDistanceKHelper(root.right, target, k)
    if rightD != -1 :
        if (rightD + 1) == k :
            print(root.data)
        else :
            nodesAtDistanceKDown(root.left, k - rightD - 2)
        return 1 + rightD

    return -1

def nodesAtDistanceKDown(root, k) :
    if root is None : 
        return

    if k == 0 :
        print(root.data)
        return

    nodesAtDistanceKDown(root.left, k - 1)
    nodesAtDistanceKDown(root.right, k - 1)

def nodesAtDistanceK(root, node, k) :
    nodesAtDistanceKHelper(root, node, k)


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
lst=[int(i) for i in input().strip().split()]
elem=lst[0]
k=lst[1]
nodesAtDistanceK(root,elem,k)

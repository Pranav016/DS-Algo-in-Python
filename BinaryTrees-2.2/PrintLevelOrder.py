# sample input - 1 2 3 4 9 5 10 6 -1 -1 -1 7 -1 -1 -1 -1 -1 -1 -1
# sample output- 
# 1 
# 2 3 
# 4 9 5 10 
# 6 7 



import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelATNewLine(root):
    if root is None:
        return
    q=queue.Queue()
    print(root.data)
    q.put(root)
    q.put(None)
    while not q.empty():
        current=q.get()
        if q.empty():
            break
        elif current is None:
            print()
            q.put(None)
        else:
            if current.left:
                q.put(current.left)
                print(current.left.data,end=" ")
            if current.right:
                q.put(current.right)
                print(current.right.data,end=" ")

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
#n=int(input())
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
printLevelATNewLine(root)

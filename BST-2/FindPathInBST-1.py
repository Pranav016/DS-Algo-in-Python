import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

lst=[]
def findPathBST(root,data):
    global lst
    if root is None:
        return 
    if root.data==data:
        lst.append(root.data)
        for i in range(len(lst)):
            print(lst.pop())
            i+=1
        return
    
    lst.append(root.data)
    findPathBST(root.left,data)
    findPathBST(root.right,data)
    if lst:
        lst.pop()
    


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
data = int(input())
# path = findPathBST(root,data)
# if path is not None:
    # for ele in path:
        # print(ele)
findPathBST(root,data)








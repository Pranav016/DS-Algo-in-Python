import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePostOrder(postorder, inorder):
    if not inorder or not postorder:
        return None
    root_data=postorder[-1]
    root=BinaryTreeNode(root_data)
    x=inorder.index(root_data)
    leftInOrder=inorder[:x]
    rightInOrder=inorder[x+1:]
    l=len(leftInOrder)
    leftPostOrder=postorder[:l]
    rightPostOrder=postorder[l:-1]
    root.left=buildTreePostOrder(leftPostOrder,leftInOrder)
    root.right=buildTreePostOrder(rightPostOrder,rightInOrder)
    return root


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

# Main
n=int(input())
postorder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postorder, inorder)
printLevelATNewLine(root)

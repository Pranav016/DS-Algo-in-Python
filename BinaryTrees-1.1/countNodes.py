class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
def treeInput():
    data=int(input())
    if data ==-1:
        return None
    root=Node(data)
    root.left=treeInput()
    root.right=treeInput()
    return root


def printTreeDetailed(root):
    if root is None:
        return
    print(root.data,end=": ")
    if root.left:
        print("L", root.left.data, end=", ")
    if root.right:
        print("R", root.right.data, end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def countNodes(root):
    if root is None:
        return 0
    left=countNodes(root.left)
    right=countNodes(root.right)
    return 1 + left + right


# main

root=treeInput()
printTreeDetailed(root)
print(countNodes(root))
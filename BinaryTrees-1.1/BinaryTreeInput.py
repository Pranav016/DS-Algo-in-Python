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


def printTree(root):
    if root is None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

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

# main

root=treeInput()
printTreeDetailed(root)
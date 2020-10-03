class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()


def printTree(root):
    if root is None: # this not base case, its an edge case
        return
    print(root.data)
    for child in root.children:
        printTree(child)

def printTreeDetailed(root):
    if root is None:
        return
    print(root.data,end=":")
    for child in root.children:
        print(child.data,end=",")

    print()

    for child in root.children:
        printTreeDetailed(child)

def treeInput():
    print("Enter root data: ")
    rootData=int(input())
    if rootData == -1:
        return None
    
    root=TreeNode(rootData)

    print("Enter the no of children of ", rootData)
    numChild=int(input())
    for i in range(numChild):
        child=treeInput()
        root.children.append(child)
        i+=1
    return root


# main
root=treeInput()
printTreeDetailed(root)
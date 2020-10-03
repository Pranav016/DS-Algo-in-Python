class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()


def printTree(root):
    if root is None:
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

    print("Enter the no of children of ", rootData," :")
    numChild=int(input())
    for i in range(numChild):
        child=treeInput()
        root.children.append(child)
        i+=1
    return root

# Method 1
def numNodes1(root):
    if root is None:
        return 0
    count=1
    for child in root.children:
        count=count+numNodes1(child)
    return count

# Method 2
count=0
def numNodes2(root):
    global count
    if root is None:
        return 0
    count+=1
    for child in root.children:
        numNodes2(child)
    return count

# main
root=treeInput()
# printTreeDetailed(root)
print(numNodes2(root))
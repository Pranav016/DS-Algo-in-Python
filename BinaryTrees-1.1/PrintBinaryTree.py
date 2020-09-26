class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
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
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)

node1.left=node2
node1.right=node3
node3.left=node4

printTreeDetailed(node1)
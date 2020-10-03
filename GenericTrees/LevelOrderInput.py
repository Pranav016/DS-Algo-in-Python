import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def printTreeDetailed(root):
    if root is None:
        return
    print(root.data,end=":")
    for child in root.children:
        print(child.data,end=",")

    print()

    for child in root.children:
        printTreeDetailed(child)

def levelOrderInput():
    q=queue.Queue()
    print("Enter root data: ")
    rootData=int(input())
    if rootData==-1:
        return None
    root=treeNode(rootData)
    q.put(root)
    while not q.empty():
        current=q.get()
        print("Enter children of ",current.data)
        numChild=int(input())
        for i in range(numChild):
            childData=int(input())
            child=treeNode(childData)
            current.children.append(child)
            q.put(child)
            i+=1
    return root


# main
root=levelOrderInput()
printTreeDetailed(root)
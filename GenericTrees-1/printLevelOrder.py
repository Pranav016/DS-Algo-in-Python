import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

def printLevelOrder(root):
    if root is None:
        return
    q=queue.Queue()
    q.put(root)
    while not q.empty():
        i=0
        current=q.get()
        print(current.data,end=":")
        for child in current.children:
            if i!=0:
                print(end=",")
            print(child.data,end="")
            q.put(child)
            i+=1
        print()

# main
arr=list(int(i) for i in input().split())
root=createLevelWiseTree(arr)
printLevelOrder(root)
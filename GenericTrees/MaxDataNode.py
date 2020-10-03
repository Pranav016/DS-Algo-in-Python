class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)
    
# Method 1
def maxDataNode1(tree):
    if not tree:
        return None
    maxNode=tree
    for child in tree.children:
        temp=maxDataNode1(child)
        if temp.data>maxNode.data:
            maxNode=temp
    return maxNode  
   
# Method 2
maxNode=None
def maxDataNode2(root):
    global maxNode
    if root is None:
        return None
    if not maxNode:
        maxNode=root
    elif root.data>maxNode.data:
        maxNode=root
    for child in root.children:
        maxDataNode2(child)
    return maxNode

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

# Main
arr = list(int(x) for x in input().strip().split(' '))
root = createLevelWiseTree(arr)
print(maxDataNode1(root).data)

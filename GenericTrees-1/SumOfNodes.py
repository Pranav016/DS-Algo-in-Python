class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def sumOfNodes(root):
    if root is None:
        return 0
    sum=root.data
    for child in root.children:
        sum=sum+sumOfNodes(child) # reaches the base case and returns the sum that is then added
    return sum

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
print(sumOfNodes(root))

# Given a tree, find and return the node for which sum of data of all children and the node itself is maximum. In the sum, data of node itself and data of immediate children is to be taken.


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def maxSumNode(root,maxSum,node):
    if root is None:
        return root,root.data
    sum=0
    sum+=root.data
    for child in root.children:
        sum+=child.data
    if sum>maxSum:
        maxSum=sum
        node=root
    for child in root.children:
        node,maxSum=maxSumNode(child,maxSum,node)
    return node,maxSum
    

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
tree = createLevelWiseTree(arr)
temp, tempSum = maxSumNode(tree,-1000000,None)
print(temp.data)

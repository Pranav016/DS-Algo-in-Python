# Given a generic tree and an integer n. Find and return the node with next larger element in the Tree i.e. find a node with value just greater than n.

# Sample Input 2 :
# 21
# 10 3 20 30 40 2 40 50 0 0 0 0 
# Sample Output 2:
# 30

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def nextLargest(root, n):
    if root is None:
        return None
    maxNum=None
    if root.data>n:
        maxNum=root
    for child in root.children:
        newNum=nextLargest(child,n)
        if not maxNum or (maxNum and newNum and maxNum.data>newNum.data):
            maxNum=newNum
    return maxNum

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
n = int(input())
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(nextLargest(tree, n).data)

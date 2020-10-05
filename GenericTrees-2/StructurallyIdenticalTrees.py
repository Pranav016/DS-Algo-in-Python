class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if (not root1 and root2) or (not root2 and root1):
        return False
    if root1.data!=root2.data:
        return False
    l1=len(root1.children)
    l2=len(root2.children)
    i=j=0
    while i<l1 and j<l2:
        child1=root1.children[i]
        child2=root2.children[j]
        i+=1
        j+=1
        return isIdentical(child1,child2)
    return True
    

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
arr1 = list(int(x) for x in input().strip().split(' '))
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in input().strip().split(' '))
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')

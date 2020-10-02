class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# worst case time complexity for all these BST functions is O(h) where h is height and best case is O(log.h)

class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    

    def printTreeHelper(self, root):
        if root == None:
            return
        print(root.data, end = ":")
        if root.left != None:
            print("L:",end='')
            print(root.left.data,end=',')
        if root.right != None:
            print("R:",end='')
            print(root.right.data,end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)
    
    
    def searchHelper(self,root,data):
        if root is None:
            return False
        if root.data==data:
            return True
        if root.data<data:
            return self.searchHelper(root.right,data)
        elif root.data>data:
            return self.searchHelper(root.left,data)

    def search(self, data):
        return self.searchHelper(self.root,data)
        

    def insertHelper(self,root,data):
        if root is None:
            root=BinaryTreeNode(data)
            return root
        if root.data<=data:
            root.right=self.insertHelper(root.right,data)
        elif root.data>data:
            root.left=self.insertHelper(root.left,data)
        return root

    def insert(self, data):
        self.root=self.insertHelper(self.root,data)
        self.numNodes+=1
        return
        

    def minimum(self,root):
        if root is None:
            return 1000000 # if right is None,we return +ve inf for root since all the elements on the left are ought to be smaller than the root

        if root.left is None:
            return root.data
        return self.minimum(root.left)

    def deleteHelper(self,root,data):
        if root is None:
            return False,None
        
        if root.data<data:
            deleted, newRightRoot=self.deleteHelper(root.right,data)
            root.right=newRightRoot
            return deleted,root
        elif root.data>data:
            deleted,newLeftRoot=self.deleteHelper(root.left,data)
            root.left=newLeftRoot
            return deleted,root
        else:
            if not root.left and not root.right:
                return True,None
            elif root.left is None:
                return True,root.right
            elif root.right is None:
                return True,root.left
            else:
                replacement=self.minimum(root.right)
                root.data=replacement
                deleted, newRightNode=self.deleteHelper(root.right,replacement)
                root.right=newRightNode
                return True,root
        

    def delete(self, data):
        deleted, newRoot=self.deleteHelper(self.root,data)
        if deleted:
            self.numNodes-=1
        self.root=newRoot
        return deleted
    

    def count(self):
        return self.numNodes


# main
b = BST()
li = [int(ele) for ele in input().split()]
i = 0
while(i < (len(li) )):
    choice = li[i]
    if choice == 1:
        data = li[i+1]
        b.insert(data)
        i+=2
    elif choice == 2:
        data = li[i+1]
        b.delete(data)
        i+=2
    elif choice == 3:
        data = li[i+1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
        i+=2
    else:
        b.printTree()
        i+=1
        
    
# Given a linked list and an integer n you need to find and return index where n is present in the LL. Do this recursively.
# Return -1 if n is not present in the LL.


from sys import setrecursionlimit

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def inputLL():
    llist=list(int(i) for i in input().split())
    head=None
    tail=None
    for data in llist:
        if data!=-1:
            newNode=Node(data)
            if head is None:
                head=newNode
                tail=newNode
            else:
                tail.next=newNode
                tail=newNode
        else:
            return head


count=0
def findNode(head,data):
    global count
    if head is None:
        return -1
    if head.data==data:
        return count
    count+=1
    return findNode(head.next,data)


# main
setrecursionlimit(1000000)
head=inputLL()
data=int(input())
print(findNode(head,data))
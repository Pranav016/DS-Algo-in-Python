import sys

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

        
        
def inputLL():
    llist=[int(i) for i in input().split()]
    head=None
    tail=None
    for data in llist:
        if data!=-1:
            newNode=Node(data)
            if head==None:
                head=newNode
                tail=newNode
            else:
                tail.next=newNode
                tail=newNode
        else:
            return head

        
def lengthLL(head):
    if head==None:
        return 0
    else:
        return 1+lengthLL(head.next)


# main
sys.setrecursionlimit(1000000)
head=inputLL()
print(lengthLL(head))
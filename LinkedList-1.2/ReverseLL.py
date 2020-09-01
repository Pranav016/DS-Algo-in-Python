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


def printReverse(head):
    if head is None:
        return 
    printReverse(head.next)
    print(head.data, end=" ")


# main
sys.setrecursionlimit(1000000)
t=int(input())
while t>0:
    head=inputLL()
    printReverse(head)
    print()
    t-=1
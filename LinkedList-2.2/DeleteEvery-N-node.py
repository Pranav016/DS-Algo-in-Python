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


def deleteN(head,m,n):
    if head is None:
        return head
    
    newHead=None
    while head is not None:
        i=0
        while i<m and head is not None:
            if newHead is None:
                newHead=head
            else:
                newHead.next=head
                newHead=newHead.next
        i=0
        while i<n and head is not None:
            head=head.next
    newHead.next=None
    return newHead

def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next
    print()

# main
head=inputLL()
m=int(input())
n=int(input())
head=deleteN(head,m,n)
printLL(head)
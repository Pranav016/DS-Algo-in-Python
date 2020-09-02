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


def reverseLL(head):
    prev=None
    curr=head
    nextL=head.next
    while curr is not None:
        curr.next=prev
        prev=curr
        curr=nextL
        if curr is not None:
            nextL=curr.next
    return prev


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next
    print()


# main
head=inputLL()
head=reverseLL(head)
printLL(head)
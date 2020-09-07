# Arrange elements in a given Linked List such that, all even numbers are placed after odd numbers. Respective order of elements should remain same.


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


def evenOdd(head):
    if head is None or head.next is None:
        return head
    oddH=None
    oddT=None
    evenH=None
    evenT=None
    while head is not None:
        if head.data%2==0:
            if evenH is None:
                evenH=head
                evenT=head
            else:
                evenT.next=head
                evenT=evenT.next
        elif head.data%2!=0:
            if oddH is None:
                oddH=head
                oddT=head
            else:
                oddT.next=head
                oddT=oddT.next
        head=head.next
    if oddH:
        oddT.next=evenH
        return oddH
    else:
        return evenH


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next
    print()

# main
head=inputLL()
head=evenOdd(head)
printLL(head)
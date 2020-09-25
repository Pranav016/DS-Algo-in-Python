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

def lengthLL(head):
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count

def bubble_sort(head):
    if head is None or head.next is None:
        return head
    n=lengthLL(head)
    for i in range(n-1):
        prev=None
        curr=head
        nex=head.next
        for j in range(n-1-i):
            if prev is None and curr.data>nex.data:
                curr.next=nex.next
                nex.next=curr
                head=nex
                prev=head
                curr=head.next
                nex=head.next.next
            elif nex.data<curr.data:
                curr.next=nex.next
                nex.next=curr
                prev.next=nex
                prev=nex
                nex=curr.next
            else:
                prev=curr
                curr=nex
                nex=nex.next
            j+=1
    return head


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next
    print()

# main
head=inputLL()
head=bubble_sort(head)
printLL(head)
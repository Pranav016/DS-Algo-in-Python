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


def midLL(head):
    if head is None or head.next is None:
        return head
    slow=head
    fast=head
    while fast.next is not None and fast.next.next is not None:
        slow=slow.next
        fast=fast.next.next
    return slow


def mergeLL(h1,h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1
    newHead=None
    newTail=None
    while h1 is not None and h2 is not None:
        if h1.data>h2.data:
            if newHead is None:
                newHead=h2
                newTail=h2
            else:
                newTail=h2
                newTail=newTail.next
            h2=h2.next
        elif h1.data<=h2.data:
            if newHead is None:
                newHead=h1
                newTail=h1
            else:
                newTail=h1
                newTail=newTail.next
            h1=h1.next

    if h1 is not None:
        newTail.next=h1
    if h2 is not None:
        newTail.next=h2

    return newHead


def mergeSort(head):
    if head is None or head.next is None:
        return head
    mid=midLL(head)
    h1=head
    h2=mid.next
    mid.next=None
    mergeSort(h1)
    mergeSort(h2)
    return mergeLL(h1,h2)


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next
    print()


# main
head=inputLL()
head=mergeSort(head)
printLL(head)
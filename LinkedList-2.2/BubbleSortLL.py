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
    l=lengthLL(head)
    i=j=0
    while i<l-1:
        j=0
        prev=None
        curr=head
        while j<l:
            if curr and curr.next and curr.data>curr.next.data:
                temp=curr.next
                if prev is None:
                    curr.next=curr.next.next
                    temp.next=curr
                    head=temp
                elif prev is not None:
                    curr.next=curr.next.next
                    temp.next=curr
                    prev.next=temp
            j+=1
            prev=curr
            if curr:
                curr=curr.next
        i+=1
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
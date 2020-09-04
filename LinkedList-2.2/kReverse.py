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


def reverseLL(head):
    if head is None or head.next is None:
        return head,head
    prev=None
    curr=head
    next1=head.next
    while curr is not None:
        curr.next=prev
        prev=curr
        curr=next1
        if curr:
            next1=curr.next
    return prev,head

def kReverse(head,i):
    if head is None or head.next is None:
        return head
    x=i
    h1=head
    t1=head
    while x>1 and t1.next is not None:
        t1=t1.next
        x-=1
    newHead=t1.next
    t1.next=None
    h1,t1=reverseLL(h1)
    t1.next=kReverse(newHead,i)
    return h1

def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next
    print()

# main
head=inputLL()
i=int(input())
head=kReverse(head,i)
printLL(head)
# Implement kReverse( int k ) in a linked list i.e. you need to reverse first K elements then reverse next k elements and join the linked list and so on.
# Indexing starts from 0. If less than k elements left in the last, you need to reverse them as well. If k is greater than length of LL, reverse the complete LL.


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
    while x>1 and t1.next is not None: # you take out the linked list of length k
        t1=t1.next
        x-=1
    newHead=t1.next # assign newHead to the head of the remaining linked list
    t1.next=None
    h1,t1=reverseLL(h1) # we reverse the linked list of length k
    t1.next=kReverse(newHead,i) # hit the base case and return the head of the reversed linked lists to be attached to the tail of the previously reversed linked lists
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
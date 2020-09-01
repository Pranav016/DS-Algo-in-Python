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
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count

def delete(head,i):
    if head==None or i>lengthLL(head)-1:
        return head
    prev=None 
    curr=head
    while i>0:
        prev=curr
        curr=curr.next
        i-=1
    if prev==None:
        head=curr.next
    else:
        prev.next=curr.next
    return head

def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next

# main
t=int(input())
while t>0:
    head=inputLL()
    print()
    i=int(input())
    head=delete(head,i)
    printLL(head)
    t-=1
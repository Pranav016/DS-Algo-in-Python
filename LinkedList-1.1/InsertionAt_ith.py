# time complexity is O(n) for worst case

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


def insertion(head,i,data):
    if i<0 or i>lengthLL(head):
        return head
    newNode=Node(data)
    if head==None:
        head=newNode
    else:
        prev=None
        curr=head
        while i>0:
            prev=curr
            curr=curr.next
            i-=1
        if prev!=None:
            prev.next=newNode
        else:
            head=newNode
        newNode.next=curr
    return head


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next

# main
t=int(input())
while t>0:
    head=inputLL()
    i=int(input())
    data=int(input())
    head=insertion(head,i,data)
    printLL(head)
    t-=1
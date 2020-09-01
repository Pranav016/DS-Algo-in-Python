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

def duplicates(head):
    if head is None or head.next is None:
        return head
    ptr=head
    while ptr.next.data==ptr.data:
        print(ptr.data)
        ptr=ptr.next
    head.next=duplicates(ptr.next)
    return head


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next
    print() 


    # main
t=int(input())
while t>0:
    head=inputLL()
    head=duplicates(head)
    # print(head.data)
    printLL(head)
    t-=1
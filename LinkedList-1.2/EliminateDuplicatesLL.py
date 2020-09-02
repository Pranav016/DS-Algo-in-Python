# You have been given a singly linked list of integers where the elements are sorted in ascending order. Write a function that removes the consecutive duplicate values such that the given list only contains unique elements and returns the head to the updated list.

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
    t1=head
    t2=head.next
    while t2!=None:
        if t1.data==t2.data:
            t2=t2.next
        else:
            t1.next=t2
            t1=t2
            t2=t2.next
    t1.next=t2
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
    printLL(head)
    t-=1
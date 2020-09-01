# You have been given a singly linked list of integers. Write a function that returns the index/position of an integer data denoted by 'N' (if it exists). Return -1 otherwise.

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


def findElement(head,data):
    count=0
    while head is not None:
        if head.data==data:
            return count
        count+=1
        head=head.next
    return -1
    


# main
t=int(input())
while t>0:
    head=inputLL()
    data=int(input())
    print(findElement(head,data))
    t-=1
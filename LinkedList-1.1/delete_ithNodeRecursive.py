import sys

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
    if i<0 or i>=lengthLL(head):
        return head
    if i==0:
        head=head.next
        return head
    head.next=delete(head.next,i-1)
    return head

def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next

# main
sys.setrecursionlimit(1000000)
head=inputLL()
i=int(input())
head=delete(head,i)
printLL(head)
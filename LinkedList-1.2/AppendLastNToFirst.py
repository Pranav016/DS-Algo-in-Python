# You have been given a singly linked list of integers along with an integer 'N'. Write a function to append the last 'N' nodes towards the front of the singly linked list and returns the new head to the list.


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


def appendLL(head,i):
    l=lengthLL(head)
    if i<0 or i>=l:
        return head
    temp=head
    p=l-i
    while temp.next!=None:
        temp=temp.next
    temp.next=head
    while p>0:
        temp=head
        head=head.next
        p-=1
    temp.next=None
    return head


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next
    print()


#main
t=int(input())
while t>0:
    head=inputLL()
    i=int(input())
    head=appendLL(head,i)
    printLL(head)
    t-=1    
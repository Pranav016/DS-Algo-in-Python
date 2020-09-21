# Sort a given linked list using Bubble Sort (iteratively). While sorting, you need to swap the entire nodes, not just the data.
# You don't need to print the elements, just sort the elements and return the head of updated LL.
# Input format : Linked list elements (separated by space and terminated by -1)`

# Sample Input 1 :
# 1 4 5 2 -1
# Sample Output 1 :
# 1 2 4 5

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
    for i in range(l):
        p1=None
        c1=head
        for j in range(l-1):
            if c1 and c1.next and c1.data>c1.next.data:
                temp=c1.next
                if p1 is None:
                    c1.next=c1.next.next
                    temp.next=c1
                    head=temp
                elif p1 is not None:
                    c1.next=c1.next.next
                    temp.next=c1
                    p1.next=temp
            j+=1
            p1=c1
            if c1:
                c1=c1.next
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
# Given a linked list, i & j, swap the nodes that are present at i & j position in the LL. You need to swap the entire nodes, not just the data.


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

def swapNodes(head,m,n):
    if head is None:
        return head
    x=m
    y=n
    m=min(x,y)
    n=max(x,y)
    i=0
    temp=head
    p1=None
    while(i<m):
        if temp is None:
            break
        p1=temp
        temp=temp.next
        i=i+1        
    c1=temp
    i=0
    temp1=head
    p2=None
    while i<n:
        if temp1 is None:
            break
        p2=temp1
        temp1=temp1.next
        i=i+1
    c2=temp1
   
    temp=c2.next
    if p1 is not None and p2 is not None:    
        p1.next=c2
        p2.next=c1
        c2.next=c1.next
        c1.next=temp
     
    if p1 is None:
        p2.next=c1
        head=c2
        c2.next=c1.next
        c1.next=temp
       
    return head
        


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next
    print()

# main
head=inputLL()
i,j=list(int(i) for i in input().split())
head=swapNodes(head,i,j)
printLL(head)
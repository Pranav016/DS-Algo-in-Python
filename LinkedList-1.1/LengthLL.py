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

# main
t=int(input())
while t>0:
    head=inputLL()
    print(lengthLL(head))
    t-=1
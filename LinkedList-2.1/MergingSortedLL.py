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


def merge(h1, h2):
    if h1 is None:
        return h2
    elif h2 is None:
        return h1
    newHead=None
    newTail=None
    while h1 is not None and h2 is not None:
        if h1.data>h2.data:
            if newHead==None:
                newHead=h2
                newTail=h2
            else:
                newTail.next=h2
                newTail=newTail.next    
            h2=h2.next    
            
        elif h1.data<=h2.data:
            if newHead==None:
                newHead=h1
                newTail=h1
            else:
                newTail.next=h1
                newTail=newTail.next
            h1=h1.next

    if h1 is not None:
        newTail.next=h1
    
    if h2 is not None:
        newTail.next=h2

    return newHead


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next
    print()

# main
head1=inputLL()
head2=inputLL()
head=merge(head1,head2)
printLL(head)
from sys import setrecursionlimit


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


def reverseLL(prev,next1): # here we are able to iterate over the LL while maintaing two pointers, prev that always is one step behind next1
    if next is None:
        global head
        head=prev
        return
    else:
        reverseLL(next1,next1.next)  # hit the base case where our next1 becomes None and prev reaches the last element, then set pointer head to prev(last element)
        next1.next=prev # after reaching base case and returning we keep on setting the next pointer of the next1 to the prev element
    

def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next
    print()


# main
setrecursionlimit(1000000)
head=inputLL()
reverseLL(None,head)
printLL(head)
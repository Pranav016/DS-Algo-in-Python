# time complexity of this approach is O(n)

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


def reverseLL(head):
    if head is None or head.next is None:
        return head
    smallhead=reverseLL(head.next)
    tail=head.next
    tail.next=head
    head.next=None
    return smallhead

def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next
    print()


# main
head=inputLL()
head=reverseLL(head)
printLL(head)
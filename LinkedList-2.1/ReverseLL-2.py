# time complexity of this apporach is O(n)

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
        return head,head
    sh,st=reverseLL(head.next) # assume that for n-1 list recursion has reversed it for you #sh=smallHead and st=smallTail
    st.next=head # set next of n-1 list to be the head
    head.next=None # set next of head to None
    return sh,head

def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head=head.next
    print()


# main
head=inputLL()
head,tail=reverseLL(head)
printLL(head)
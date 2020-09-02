# You have been given a head to a singly linked list of integers. Write a function check to whether the list given is a 'Palindrome' or not.

# time complexity is O(n) and space complexity is O(1)

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


def reverseLL(head):
    if head is None or head.next is None:
        return head
    prev=None
    next1=head.next
    while head is not None:
        head.next=prev
        prev=head
        head=next1
        if head is not None:
            next1=head.next
    return prev



def pallindrome(h1):
    if head is None or head.next is None:
        return True
    mid=lengthLL(head)//2
    h2=h1
    temp=None
    while mid>0:
        temp=h2
        h2=h2.next
        mid-=1
    temp.next=None
    h2=reverseLL(h2)
    while h1 is not None and h2 is not None:
        if h1.data!=h2.data:
            return False
        else:
            h1=h1.next
            h2=h2.next
    return True


    # main
t=int(input())
while t>0:
    head=inputLL()
    if pallindrome(head):
        print("true")
    else:
        print("false")
    t-=1
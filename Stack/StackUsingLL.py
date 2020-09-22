# stack implementation using Linked list

from sys import stdin

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:

    def __init__(self):
        self.__count=0
        self.__head=None

    def push(self,data):
        newNode=Node(data)
        newNode.next=self.__head
        self.__head=newNode
        self.__count+=1
        
    def pop(self):
        if self.isEmpty():
            return -1
        else:
            temp=self.__head
            self.__head=self.__head.next
            self.__count-=1
            return temp.data

    def top(self):
        if self.isEmpty():
            return -1
        else:
            return self.__head.data
        
    def getSize(self):
        return self.__count
    
    def isEmpty(self):
        return self.__count==0

    
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2 :
        print(stack.pop())

    elif choice == 3 :
        print(stack.top())

    elif choice == 4 : 
        print(stack.getSize())

    else :
        if stack.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1
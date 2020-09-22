import sys

def pushBottom(stack,item): # this function helps to insert at the bottom by emptying the stack and then pushing the element
    if not stack:
        stack.append(item) # here stack is empty and we insert our element
        return
    top=stack.pop() 
    pushBottom(stack,item) 
    stack.append(top)

def reverse(stack):
    if not stack: # if there is no element then it is already reversed
        return
    top=stack.pop() # we keep the top element
    reverse(stack) # use recursion to hit the base case to empty the stack
    pushBottom(stack,top) # push the element from the top to the bottom

#main
sys.setrecursionlimit(10000000)
stack=[]
n=int(input())
ele=list(int(i) for i in input().split())
for i in ele:
    stack.append(i)
reverse(stack)
while stack:
    print(stack.pop(), end=" ")
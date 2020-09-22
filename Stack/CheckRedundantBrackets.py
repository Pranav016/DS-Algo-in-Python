
from sys import stdin

def checkRedundant(stack):
    if not stack:
        return 
    c=0
    z=4
    x=stack.pop()
    if x==')':
        y=stack.pop()
        while stack and y!='(':
            c+=1
            if y==')':
                print(*stack)
                z=checkRedundant(stack)
            y=stack.pop()
        if not z:
            if stack and c!=0:
                return False
            elif stack and c==0:
                return True
            elif not stack and c!=0:
                return False
        else:
            return True

#main
s = stdin.readline().strip()
stack=[]
for i in s:
    stack.append(i)
if checkRedundant(stack) :
	print("true")

else :
	print("false")

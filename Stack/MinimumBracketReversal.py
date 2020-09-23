def bracketReversal(stack):
    if len(stack)%2!=0:
        return -1
    l=len(s)//2
    i=0
    c=0
    while i<l:
        x=stack.pop()
        if x!=')':
            c+=1
        i+=1
    i=0
    while i<l:
        x=stack.pop()
        if x!='(':
            c+=1
        i+=1
    return c


# main
s=str(input())
s=list(s)
print(bracketReversal(s))
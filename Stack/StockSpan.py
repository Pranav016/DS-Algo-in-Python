def stockSpan(stock):
    if not stock:
        return 
    span=[]
    stack=[]
    i=0
    while i<len(stock):
        if not stack:
            stack.append(i)
            span.append(i+1)
        else:
            if stock[stack[-1]]>=stock[i]:
                span.append(i-stack[-1])
                stack.append(i)
            elif stock[stack[-1]]<stock[i]:
                c=0
                while stack and stock[i]>stock[stack[-1]]:
                    c+=1
                    stack.pop()
                if not stack:
                    span.append(i+1)
                else:
                    span.append(c+1)
                stack.append(i)
        i+=1
    
    return span


# main
n=int(input())
stock=[]
if n>0:
    ele=list(int(i) for i in input().split())
    for i in ele:
        stock.append(i)
    span=stockSpan(stock)
    print(*span)

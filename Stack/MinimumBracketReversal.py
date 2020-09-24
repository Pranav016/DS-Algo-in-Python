# For a given expression in the form of a string, find the minimum number of brackets that can be reversed in order to make the expression balanced. The expression will only contain curly brackets.
# If the expression can't be balanced, return -1.

# Expression: {{{{
# If we reverse the second and the fourth opening brackets, the whole expression will get balanced. Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.

# Expression: {{{
# In this example, even if we reverse the last opening bracket, we would be left with the first opening bracket and hence will not be able to make the expression balanced and the output will be -1.

def bracketReversal(s):
    if len(s)%2!=0:
        return -1
    stack=[]
    i=0
    while i<len(s):
        if not stack:
            stack.append(s[i])
        else:
            if s[i]=='{':
                stack.append(s[i])
            elif s[i]=='}':
                if stack[-1]=='{':
                    stack.pop()
                else:
                    stack.append(s[i])
        i+=1
    c=0
    while stack:
        x=stack.pop()
        y=stack.pop()
        if x==y:
            c+=1
        elif x=='{' and y=='}':
            c+=2
    return c


# main
s=str(input())
s=list(s)
print(bracketReversal(s))
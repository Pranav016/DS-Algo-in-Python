# For a given expression in the form of a string, find if there exist any redundant brackets or not. It is given that the expression contains only rounded brackets or parenthesis and the input expression will always be balanced.
# A pair of the bracket is said to be redundant when a sub-expression is surrounded by unnecessary or needless brackets.

# Expression: (a+b)+c
# Since there are no needless brackets, hence, the output must be 'false'.

# Expression: ((a+b))
# The expression can be reduced to (a+b). Hence the expression has redundant brackets and the output will be 'true'.


from sys import stdin

def checkRedundant(s):
    if not s:
        return False
    stack=[]
    c=0
    i=0
    while i<len(s):
        if s[i]==')':
            x=stack.pop()
            while x!='(' and stack:
                c+=1
                x=stack.pop()
            if c>1 and x=='(':
                c=0
                i+=1
                continue
            else:
                return True
        else:
            stack.append(s[i])
        i+=1
    return False

    

#main
s = stdin.readline().strip()
if checkRedundant(s) :
	print("true")
else :
	print("false")

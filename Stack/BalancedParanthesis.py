def balanced(s):
    stack=[]

    for char in s:
        if char in '{([':
            stack.append(char)
        elif char==')':
            if not stack or stack[-1]!='(':
                return False
            stack.pop()
        elif char==']':
            if not stack or stack[-1]!='[':
                return False
            stack.pop()
        elif char=='}':
            if not stack or stack[-1]!='{':
                return False
            stack.pop()

    if not stack:
        return True
    return False

# main

s=str(input())
if balanced(s):
    print("true")
else:
    print("false")
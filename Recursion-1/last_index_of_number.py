# the logic for this question- 
# I am first hitting the base case as seen in statement 1 thus reaching the last element of the array and returning -1
# If I am returning -1 then I keep on checking for x in the array as I iterate over the array in reverse order as seen in statement 2
# As soon as I find the index of the element x from the last, I am returning 0 and then +1 on each iteration as seen in statement 3
# Now that I have found the index of element from the last, I am not checking for any other index since -1 is never returned thus the control does not go into the if statement at statement 4 thus the last index of x in the array is returned.

def lastIndex(a, x):
    if len(a)==0:
        return -1
    
    smallList=lastIndex(a[1:], x)  # Statement 1

    if smallList==-1: # Statement 4
        if a[0]==x:   # Statement 2
            return 0
        else:
            return -1
    else:
        return smallList+1 # Statement 3
    
n=int(input())
a= list(int(i) for i in input().strip().split(' '))
x=int(input())
print(lastIndex(a,x))
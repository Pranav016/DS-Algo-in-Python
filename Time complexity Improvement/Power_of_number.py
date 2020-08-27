# Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to return the answer.
# Do this recursively.

# time complexity of this solution has been reduced

def power(x, n):
    if n<=0:
        return 1
    smallpower=power(x,n//2)
    if n%2==0:
        return smallpower*smallpower
    if n%2!=0:
        return smallpower*smallpower*x

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x,n))
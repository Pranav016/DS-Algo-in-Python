# Given an integer N, count and return the number of zeros that are present in the given integer using recursion.

c=0
def countz(n):
    if n>0:
        global c
        if n%10==0:
            c+=1
        countz(n//10)
    return c

n=int(input())
print(countz(n))



#alternate method-

def countzeros(n):
    if n<10:
        if n==0:
            return 1
        else:
            return 0
    smalloutput = countzeros(n//10)
    if n%10==0:
        smalloutput +=1
    return smalloutput 

    

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
print(countzeros(n))

#sample input- 10204
# sample output- 2
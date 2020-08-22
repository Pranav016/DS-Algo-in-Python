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
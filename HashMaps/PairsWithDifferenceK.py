# You are given with an array of integers and an integer K. Write a program to find and print all pairs which have difference K.
# Take difference as absolute.


def printPairDiffK(l, k):
    d={}
    for w in l:
        d[w]=d.get(w,0)+1
    if k==0:
        n=d[w]-1
        for i in range(n*(n+1)//2):
            print(w,w)
        return

    for i in l:
        diff=i-k
        if diff in d:
            x=d[diff]
            y=d[i]
            for j in range(x*y):
                print(diff,i)
                j+=1
        diff=i+k
        if diff in d:
            x=d[diff]
            y=d[i]
            for j in range(x*y):
                print(i,diff)
                j+=1
        d[i]=0
        i+=1


# main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
printPairDiffK(l, k)
# sample test case-
# 9
# 1 3 6 2 5 4 3 2 4
# 7
# sample output-
# 1 6
# 3 4
# 3 4
# 2 5
# 2 5
# 3 4
# 3 4

def merge(a,x,y):
    i=j=k=0
    while i<len(x) and j<len(y):
        if x[i]>y[j]:
            a[k]=y[j]
            k+=1
            j+=1
        else:
            a[k]=x[i]
            k+=1
            i+=1
    while i<len(x):
        a[k]=x[i]
        k+=1
        i+=1
    while j<len(y):
        a[k]=y[j]
        k+=1
        j+=1

def merge_sort(a):
    if len(a)==0 or len(a)==1:
        return
    mid=len(a)//2
    x=a[:mid]
    y=a[mid:]
    merge_sort(x)
    merge_sort(y)
    merge(a,x,y)

def pairSum(a, x):
    merge_sort(a)
    i=0
    j=len(a)-1
    while i<j:
        if a[i]+a[j]>x:
            j-=1
        elif a[i]+a[j]<x:
            i+=1
        elif a[i]+a[j]==x:
            print("{} {}".format(a[i],a[j]))
            k=j
            while a[k]!=a[k-1]:
                    print("{} {}".format(a[i],a[k]))
                    k-=1
            if a[i]==a[i+1]:
                if k==j:
                    j+=1
                    i+=1
                else:
                    i+=1

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
pairSum(arr, sum)

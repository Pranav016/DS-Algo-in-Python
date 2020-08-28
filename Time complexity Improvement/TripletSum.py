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

def triplet(a,x):
    merge_sort(a)
    i=0
    j=len(a)-1
    k=len(a)//2
    while i<j:
        # print("all- {} {} {}".format(a[i],a[k],a[j]))
        if k<=i or k>=j:
            i+=1
            j=len(a)-1
            k=len(a)//2
        elif a[i]+a[j]+a[k]>x:
            k-=1
        elif a[i]+a[j]+a[k]<x:
            k+=1
        elif a[i]+a[j]+a[k]==x:
            print("{} {} {}".format(a[i],a[k],a[j]))
            j-=1
            k=len(a)//2
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
triplet(arr, sum)

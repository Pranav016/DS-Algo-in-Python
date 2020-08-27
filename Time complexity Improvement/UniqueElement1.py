# Time complexity of this approach is O(nlog(n))

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

def FindUnique(arr):
    if len(arr)<=1:
        return arr
    merge_sort(arr)
    j=k=0
    for i in range(0,len(arr)):
        j=i-1
        k=i+1
        if j==-1:
            if arr[i]!=arr[k]:
                return arr[i]
        elif k>=len(arr):
            if arr[i]!=arr[j]:
                return arr[i]
        elif arr[i]!=arr[j] and arr[i]!=arr[k]:
            return arr[i]
        

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
unique=FindUnique(arr)
print(unique)

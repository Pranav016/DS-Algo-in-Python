def common(a,b):
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]==b[j]:
            print(a[i])
            i+=1
            j+=1
        elif a[i]>b[j]:
            j+=1
        else:
            i+=1
def merge(s1,s2,arr):
    i=j=k=0
    while i<len(s1) and j<len(s2):
        if s1[i]>s2[j]:
            arr[k]=s2[j]
            k+=1
            j+=1
        else:
            arr[k]=s1[i]
            k+=1
            i+=1
    while i<len(s1):
        arr[k]=s1[i]
        i+=1
        k+=1
    while j<len(s2): 
        arr[k]=s2[j]
        k+=1
        j+=1

def merge_sort(arr):
    if len(arr)==0 or len(arr)==1:
        return     
    mid=len(arr)//2
    s1=arr[0:mid] 
    s2=arr[mid:]
    merge_sort(s1) 
    merge_sort(s2) 
    merge(s1,s2,arr)

def intersection(arr1, arr2):
    if len(arr1)==0 or len(arr2)==0:
        return
    merge_sort(arr1)
    merge_sort(arr2)
    common(arr1,arr2)

# Main
n1=int(input())
arr1=list(int(i) for i in input().strip().split(' '))
n2=int(input())
arr2=list(int(i) for i in input().strip().split(' '))
intersection(arr1, arr2) 

def merge(s1,s2,arr):
    i=j=k=0
    while i<len(s1) and j<len(s2): # such that if either list gets exhausted then the loop stops
        if s1[i]>s2[j]:
            arr[k]=s2[j]
            k+=1
            j+=1
        else:
            arr[k]=s1[i]
            k+=1
            i+=1
    while i<len(s1): # if above loop is exited for s2 being exhausted
        arr[k]=s1[i]
        i+=1
        k+=1
    while j<len(s2): # if above loop is exited for s1 being exhausted
        arr[k]=s2[j]
        k+=1
        j+=1

def mergeSort(arr):
    if len(arr)==0 or len(arr)==1:
        return      # we are returning at len of arr==0 or len of arr==1 because array with 0 or 1 element will always be sorted
    mid=len(arr)//2
    s1=arr[0:mid]  # we are slicing from 0 and not from a variable 'start' because in python recursion, each call gives us a new copy of the shortened list thus we can slice from 0 to mid because 0th element keeps on changing for every new copy of the list
    s2=arr[mid:]
    mergeSort(s1) # this call will hit the base case and return a single element in s1 to merge with s2
    mergeSort(s2) # this call will hit the base case and return a single element in s2 to merge with s1
    merge(s1,s2,arr)

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)
def partition(a,si,ei): # the partiton function is going to move the elements smaller than the pivot to the left of it and the elements larger than the pivot to the right of it
    pivot=a[si]
    c=0
    for i in range(si,ei+1):
        if a[i]<pivot:
            c+=1
    a[si+c],a[si]=a[si],a[si+c]
    pivot_index=si+c
    i=si
    j=ei
    while i<j:
        if pivot>a[i]:
            i+=1
        elif pivot<=a[j]:
            j-=1
        else:
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
    return pivot_index


def quick_sort(a,si,ei): # si=start index and ei=end index
    if si>=ei:  # base case
        return

    p=partition(a,si,ei) # getting the partition of the list
    quick_sort(a,si,p-1) # call quick_sort on left side of the partition
    quick_sort(a,p+1,ei) # call quick sort on right side of the partition


#main
n=int(input())
a=list(int(i) for i in input().strip().split(' '))
quick_sort(a,0,len(a)-1)
print(*a)
# to check if a list or an array is sorted or not

def isSorted(a,i):
    l=len(a)
    if i==l-1:
        return True
    if a[i]>a[i+1]:
        return False
    return isSorted(a,i+1)
a=[1,2,3,4,5,6]
print(isSorted(a,0))
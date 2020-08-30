# Find and return the equilibrium index of an array. Equilibrium index of an array is an index i such that the sum of elements at indices less than i is equal to the sum of elements at indices greater than i.
# Element at index i is not included in either part.
# If more than one equilibrium index is present, you need to return the first one. And return -1 if no equilibrium index is present.

# time complexity of this solution is O(n)

left=0
right=0
def lsum(a,s,e):
    global left
    if e>=0:
        left+=a[e]
        return left

def rsum(a,s,e):
    global right
    if s==1:
        return right
    else:
        right=right-a[s-1]
        return right

def equilibriumIndex(arr):
    if len(arr)<=1:
        return -1
    for i in range(len(arr)):
        l=lsum(arr,0,i-1)
        r=rsum(arr,i+1,len(arr)-1)
        if l==r:
            return i

# Main
n = int(input())
arr = [int(i) for i in input().strip().split()]
for i in range(1,len(arr)):
    right+=arr[i]
print(equilibriumIndex(arr))

# Given an integer array of size 2N + 1. In this given array, N numbers are present twice and one number is present only once in the array.
# You need to find and return that number which is unique in the array.

# Time complexity of this approach is O(n)

# solution- any number xor with 0 is 0 and xor of two same numbers is 0/ xor of two different numbers is 1

def unique(a):
    if len(a)==1:
        return a
    ans=0
    for i in range(len(a)):
        ans=ans^a[i]
    return ans

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(unique(arr))
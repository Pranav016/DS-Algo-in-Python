# Given an array of integers of size n which contains numbers from 0 to n - 2. Each number is present at least once. That is, if n = 5, numbers from 0 to 3 is present in the given array at least once and one number is present twice. You need to find and return that duplicate number present in the array.
# Assume, duplicate number is always present in the array.

# Solution = sum of natural numbers from 1 to n - sum inputed

# time complexity is O(n)


def MissingNumber(a,n):
    ans1=0
    ans2=0
    for i in range(n-1):
        ans1=ans1+i
    for i in range(n):
        ans2=ans2+a[i]
    return ans2-ans1
    

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
ans=MissingNumber(arr,n)
print(ans)

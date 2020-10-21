# MCM= Matrix Chain Multiplication
# Basically we have to virtually place brackets during multiplication of matrices thus giving us the lowest possible operations(cost) that are needed to be done.


import sys


def mcm(arr,i,j):

    if i>=j:
        return 0

    ans=sys.maxsize

    for k in range(i,j): # this loop helps us in placing brackets at different positions
        ans1=mcm(arr,i,k) # gives min cost for left part
        ans2=mcm(arr,k+1,j) # gives min cost for right part
        ans3=arr[i-1]*arr[k]*arr[j] # gives min cost for resultant matrices from left and right part
        cost=ans1+ans2+ans3 # this the total cost of putting brackets in a particular way
        ans=min(ans,cost)
    return ans
    


# main
n=int(input())
arr=[int(i) for i in input().split()]
print(mcm(arr,1,n))

import sys


def mcm(arr,i,j,dp):

    if i>=j:
        return 0

    ans=sys.maxsize

    for k in range(i,j):
        if dp[i][k]!=-1:
            ans1=dp[i][k]
        else:
            ans1=mcm(arr,i,k,dp)
            dp[i][k]=ans1

        if dp[k+1][j]!=-1:
            ans2=dp[k+1][j]
        else:
            ans2=mcm(arr,k+1,j,dp)
            dp[k+1][j]=ans2
        
        ans3=arr[i-1]*arr[k]*arr[j]
        cost=ans1+ans2+ans3
        ans=min(ans,cost)
    
    return ans
    


# main
n=int(input())
arr=[int(i) for i in input().split()]
dp=[[-1 for j in range(n+1)]for i in range(n+1)]
print(mcm(arr,1,n,dp))
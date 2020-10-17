# Method 2 is better 


import sys

# Method 1


def minStepsA(n,dp):
    
    if n<=1:
        return dp[n]
    
    if dp[n]!=-1:
        return dp[n]

    ans1=ans2=ans3=sys.maxsize

    ans1=minStepsA(n-1,dp)

    if n%2==0:
        ans2=minStepsA(n//2,dp)
    if n%3==0:
        ans3=minStepsA(n//3,dp)
    
    ans=min(ans1,ans2,ans3)+1
    dp[n]=ans
    return ans

# Method-2 

def minStepsB(n,dp):
    if n==1:
        return 0
    
    if dp[n-1]==-1:
        ans1=minStepsB(n-1,dp) # this will always give an ans
        dp[n-1]=ans1
    else:
        ans1=dp[n-1]

    ans2=sys.maxsize
    if n%2==0:
        if dp[n//2]==-1:
            ans2=minStepsB(n//2,dp)
            dp[n//2]=ans2
        else:
            ans2=dp[n//2]

    ans3=sys.maxsize
    if n%3==0:
        if dp[n//3]==-1:
            ans3=minStepsB(n//3,dp)
            dp[n//3]=ans3
        else:
            ans3=dp[n//3]

    ans=1+min(ans1,ans2,ans3)
    return ans
    

# main
sys.setrecursionlimit(1000000)
n=int(input())
dp=[-1 for i in range(n+1)]
dp[0]=dp[1]=0
print(minStepsB(n,dp))
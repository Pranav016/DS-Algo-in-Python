# Given a positive integer 'n', find and return the minimum number of steps that 'n' has to take to get reduced to 1. You can perform any one of the following 3 steps:
# 1.) Subtract 1 from it. (n = n - ­1) ,
# 2.) If n is divisible by 2, divide by 2.( if n % 2 == 0, then n = n / 2 ) ,
# 3.) If n is divisible by 3, divide by 3. (if n % 3 == 0, then n = n / 3 ).  



import sys

def minSteps(n,dp):
    if n==1:
        return 0
    
    if dp[n-1]==-1:
        ans1=minSteps(n-1,dp) # this will always give an ans
        dp[n-1]=ans1
    else:
        ans1=dp[n-1]

    ans2=sys.maxsize
    if n%2==0:
        if dp[n//2]==-1:
            ans2=minSteps(n//2,dp)
            dp[n//2]=ans2
        else:
            ans2=dp[n//2]

    ans3=sys.maxsize
    if n%3==0:
        if dp[n//3]==-1:
            ans3=minSteps(n//3,dp)
            dp[n//3]=ans3
        else:
            ans3=dp[n//3]

    ans=1+min(ans1,ans2,ans3)
    return ans
    
    

# main
sys.setrecursionlimit(1000000)
n=int(input())
dp=[-1 for i in range(n+1)]
print(minSteps(n,dp))
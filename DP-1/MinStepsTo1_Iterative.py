import sys

def minStepsIterative(n):
    dp=[-1 for i in range(n+1)]
    dp[0]=dp[1]=0
    for i in range(2,n+1):
        ans1=ans2=ans3=sys.maxsize
        if i%3==0:
            if i//3==1:
                ans1=dp[i//3]
                dp[i//3]=ans1
            else:
                ans1=dp[i//3]
        if i%2==0:
            if i//2==1:
                ans2=dp[i//2]
                dp[i//2]=ans2
            else:
                ans2=dp[i//2]
        
        ans3=dp[i-1]
        dp[i]=1+min(ans1,ans2,ans3)
    return dp[n]


# main
n=int(input())
print(minStepsIterative(n))
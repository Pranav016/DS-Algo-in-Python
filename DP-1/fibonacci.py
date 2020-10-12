# for nth fibonacci no. we are making total (n-1) recursive calls
# our time complexity has gone done from O(2^n) to O(n)
# space complexity is same O(n)

# saving overlapping subproblems is called Memoization


def fib(n,dp):
    if dp[n-1]==-1:
        ans1=fib(n-1,dp)
        dp[n-1]=ans1
    else:
        ans1=dp[n-1]
    if dp[n-2]==-1:
        ans2=fib(n-2,dp)
        dp[n-2]=ans2
    else:
        ans2=dp[n-2]
    return ans1 + ans2


# main
n=int(input())
dp=[-1 for i in range(n+1)]
dp[0]=0
dp[1]=1
print(fib(n,dp))
# time complexity is O(n)
# Iterative method is better because it does not experience the problem of stack overflow


def fibIterative(n):
    dp=[-1 for i in range(n+1)]
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
        i+=1
    return dp[n]


# main
n=int(input())
print(fibIterative(n))
# for memoization table/ matrix/ array, always check those variables in the function that are changing


def knapsack(wt,val,cap,n,dp):

    # base case
    if n==0 or cap==0:
        return 0

    # applying DP
    if dp[cap][n]!=-1:
        return dp[cap][n]
    
    if wt[n-1]<=cap:
        includeThisWt = val[n-1] + knapsack(wt,val,cap-wt[n-1],n-1,dp)
        notIncludeThisWt = knapsack(wt,val,cap,n-1,dp)
        ans = max(includeThisWt, notIncludeThisWt)
        dp[cap][n] = ans
        return ans
    else:
        ans=knapsack(wt,val,cap,n-1,dp)
        dp[cap][n]=ans
        return ans



# main
n=int(input()) # size of the array
wt=list(int(i) for i in input().split())
val=list(int(i) for i in input().split())
cap=int(input()) # capacity of the knapsack
dp=[[-1 for j in range(n+1)]for i in range((cap+1))]
print(knapsack(wt,val,cap,n,dp))
def knapsack(weights,values,capacity,n,dp):
    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if weights[i-1]<=j: # starting from i-1 because loop for i starts from 1 and we could miss the weights on 0-th pos
                includeWt=values[i-1]+dp[i-1][j-weights[i-1]]
                notIncludeWt=dp[i-1][j]
                dp[i][j]=max(includeWt,notIncludeWt)
            else:
                dp[i][j]=dp[i-1][j]
    
    return dp[n][capacity]


# main
n=int(input())
weights=list(int(i) for i in input().split())
values=list(int(i) for i in input().split())
capacity=int(input())
dp=[[0 for j in range(capacity+1)]for i in range((n+1))]
print(knapsack(weights,values,capacity,n,dp))
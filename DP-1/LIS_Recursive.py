def lis(lst,i,n,dp):
    if i==n:
        return

    for j in range(i+1):
        if lst[j]<lst[i]:
            if 1+dp[j]>dp[i]:
                dp[i]=1+dp[j]
    
    lis(lst,i+1,n,dp)
    return max(dp)


# main
n=int(input())
lst=list(int(i) for i in input().split())
dp=[1 for i in range(n+1)]
print(lis(lst,0,n,dp))
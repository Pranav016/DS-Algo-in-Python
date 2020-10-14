# Longest Increasing subsequence problem using DP
# We check for elements before j and check if they are smaller than lst[j]. Then we compare the longest subsequence they are forming and if they are less than lst[j] and (their subsequence + 1) is greater than subsequence of j then we update subsequence of j in dp array.


def lis(lst,n):
    dp=[1 for i in range(n+1)]
    j=1
    while j<n:
        for i in range(j+1):
            if lst[j]>lst[i]:
                if 1+dp[i]>dp[j]:
                    dp[j]=dp[i]+1
        j+=1
    
    return max(dp)




# main
n=int(input())
lst=list(int(i) for i in input().split())
print(lis(lst,n))
# time complexity is O(n.sqrt(n)) and space complexity is O(n)


import math
import sys

def minSquares(n):
    dp=[-1 for i in range(n+1)]
    dp[0]=0
    for i in range(1,n+1):
        minEle=sys.maxsize
        root=int(math.sqrt(i))
        for j in range(1,root+1):
            ans=1+dp[i-(j**2)]
            minEle=min(ans,minEle)
        dp[i]=minEle
    
    return dp[n]


# main
n=int(input())
print(minSquares(n))
        

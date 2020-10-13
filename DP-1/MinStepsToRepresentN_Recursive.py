# A number can always be represented as a sum of squares of other numbers. Note that 1 is a square and we can always break a number as [(1 * 1) + (1 * 1) + (1 * 1) + …]. Given a number n, find the minimum number of squares that sum to n.


import sys

def minSquares(n,dp):
    if n==0:
        return 0
    i=1
    minEle=sys.maxsize
    while i**2<=n:
        if dp[n-(i**2)]==-1:
           ans= 1+minSquares(n-(i**2),dp)
        else:
            ans=1+dp[n-(i**2)]
        if ans<minEle:
            minEle=ans
        i+=1
    dp[n]=minEle
    return dp[n]


# main
sys.setrecursionlimit(1000000)
n=int(input())
dp=[-1 for i in range(n+1)]
print(minSquares(n,dp))

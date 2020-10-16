# A number can always be represented as a sum of squares of other numbers. Note that 1 is a square and we can always break a number as [(1 * 1) + (1 * 1) + (1 * 1) + …]. Given a number n, find the minimum number of squares that sum to n.


import math,sys

def minSquares(n):
    if n==0:
        return 0

    ans=sys.maxsize
    root=int(math.sqrt(n))
    for i in range(1,root+1):
        currans=1+minSquares(n-i**2)
        ans=min(currans,ans)

    return ans

# main
sys.setrecursionlimit(1000000)
n=int(input())
print(minSquares(n))

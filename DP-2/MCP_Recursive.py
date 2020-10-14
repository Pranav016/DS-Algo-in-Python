# MIC- Minimum Cost Path problem

import sys

def mic(i,j,m,n,lst):
    
    # corner case
    if i==m-1 and j==n-1:
        return lst[i][j]

    # base case
    if i>=m or j>=n:
        return sys.maxsize

    # options
    a=mic(i+1,j,m,n,lst)
    b=mic(i,j+1,m,n,lst)
    c=mic(i+1,j+1,m,n,lst)

    ans=lst[i][j]+min(a,b,c)
    return ans
    


# main
m,n=map(int, input().split())
lst=[[3,4,1,2],[2,1,8,9],[4,7,8,1]]
ans=mic(0,0,m,n,lst)
print(ans)
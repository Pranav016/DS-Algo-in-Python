# MIC- Minimum Cost Path problem

import sys

def mcp(mat,i,j,n,m,dp):

    if i==n-1 and j==m-1:
        return mat[i][j]

    if i>=n or j>=m:
        return sys.maxsize

    if dp[i+1][j]!=sys.maxsize:
        costDown=dp[i+1][j]
    else:
        costDown=mcp(mat,i+1,j,n,m,dp)

    if dp[i][j+1]!=sys.maxsize:
        costUp=dp[i][j+1]
    else:
        costUp=mcp(mat,i,j+1,n,m,dp)
    if dp[i+1][j+1]!=sys.maxsize:
        costDiagonal=dp[i+1][j+1]
    else:
        costDiagonal=mcp(mat,i+1,j+1,n,m,dp)
    minCostAtPos=mat[i][j]+min(costDown,costUp,costDiagonal)
    dp[i][j]=minCostAtPos
    return dp[i][j]
    

def take2DInput() :
    li = sys.stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
mat,n,m=take2DInput()
dp=[[sys.maxsize for j in range(m+1)]for i in range(n+1)]
print(mcp(mat,0,0,n,m,dp))
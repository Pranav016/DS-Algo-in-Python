# MIC- Minimum Cost Path problem

import sys

def mcp(mat,i,j,n,m,dp):
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if i==n-1 and j==m-1:
                dp[i][j]=mat[i][j]
            else:
                CostRight=dp[i+1][j]
                costDown=dp[i][j+1]
                costDiagonal=dp[i+1][j+1]
                dp[i][j]=mat[i][j]+min(CostRight,costDown,costDiagonal)

    return dp[0][0]


# def mcp2(mat,i,j,n,m,dp):
#     for i in range(n):
#         for j in range(m):
#             if i==0 and j==0:
#                 dp[i][j]=mat[0][0]
#             else:
#                 costLeft=dp[i-1][j]
#                 costUp=dp[i][j-1]
#                 costDiagonal=dp[i-1][j-1]
#                 dp[i][j]=mat[i][j]+min(costLeft,costUp,costDiagonal)

#     return dp[n-1][m-1]
    

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
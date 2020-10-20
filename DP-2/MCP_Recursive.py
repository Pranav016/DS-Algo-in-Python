# MIC- Minimum Cost Path problem

import sys

def mcp(mat,i,j,n,m):
    
    if i==n or j==m:
        return sys.maxsize

    if i==n-1 and j==m-1:
        return mat[i][j]

    costDown=mcp(mat,i+1,j,n,m)
    costUp=mcp(mat,i,j+1,n,m)
    costDiagonal=mcp(mat,i+1,j+1,n,m)
    costAtPos=mat[i][j]+min(costDown,costUp,costDiagonal)
    return costAtPos
    

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
print(mcp(mat,0,0,n,m))
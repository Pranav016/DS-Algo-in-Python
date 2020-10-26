def isSafeToPut(i,j,n,solution):

    k=i-1
    while k>=0:
        if solution[k][j]:
            return False
        k-=1

    k=j+1
    while k<n:
        if solution[i][k]:
            return False
        k+=1

    row=i-1
    col=j-1
    while row>=0 and col>=0:
        if solution[row][col]:
            return False
        row-=1
        col-=1

    row=i-1
    col=j+1
    while row>=0 and col<n:
        if solution[row][col]:
            return False
        row-=1
        col+=1

    return True


def nqueen(solution,n,i):
    if i==n:
        for i in range(n):
            for j in range(n):
                print(solution[i][j],end=" ")
        print()
        return False

    for j in range(n):
        solution[i][j]=1
        if isSafeToPut(i,j,n,solution):
            if nqueen(solution,n,i+1):
                return True
        solution[i][j]=0

    return False
    


# main
n=int(input())
solution=[[0 for j in range(n)]for i in range(n)]
nqueen(solution,n,0)

import sys
sys.setrecursionlimit(10**6)

def subsetSumK(arr,k):
    ans=fxn(arr,k,[],[])
    for i in ans:
        for j in i:
            print(j,end=" ")
        print()

def fxn(arr,k,l,main):
    if k==0:
        main.append(l)
        return
    if k<0:
        return
    if len(arr)==0:
        return
    new=l.copy()
    new.append(arr[0])
    fxn(arr[1:],k-arr[0],new,main)
    fxn(arr[1:],k,l,main)
    return main
    


def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


#main
arr, n = takeInput()

if n != 0 :
    k = int(input().strip())
    subsetSumK(arr, k)

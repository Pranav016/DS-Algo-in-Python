

def printSubsets(arr,ans):
    if len(arr)==0:
        print(ans[1:])
        return

    printSubsets(arr[1:],ans)
    printSubsets(arr[1:],ans+" "+str(arr[0]))


# main
n=int(input())
arr=[int(i) for i in input().split()]
printSubsets(arr,"")
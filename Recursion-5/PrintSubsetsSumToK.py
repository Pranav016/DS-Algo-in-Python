
def subsetSum(arr,k,ans):
    if k==0:
        print(ans[1:])
        return
    if k<0:
        return
    if len(arr)<=0:
        return

    subsetSum(arr[1:],k,ans)
    subsetSum(arr[1:],k-arr[0],ans+" "+str(arr[0]))


# main
n=int(input())
arr=[int(i) for i in input().split()]
k=int(input())
subsetSum(arr,k,"")
def subsets(arr):
    if len(arr)==0:
        output=[""]
        return output

    smallOutput=arr[1:]
    smallOutput=subsets(smallOutput)
    output=[]
    for ele in smallOutput:
        output.append(ele)
    for ele in smallOutput:
        output.append(str(arr[0])+" "+ele)
    return output


# main
n=int(input())
arr=[int(i) for i in input().split()]
ans=subsets(arr)
for ele in ans:
    print(ele)
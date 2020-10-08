
def subsetSum(l):
    d={}
    sum=0
    maxLen=-1000000
    subsetLen=-1000000
    for i in range(len(l)):
        sum+=l[i]
        print(sum)
        if d.get(sum,False)==False:
            if sum==0:
                subsetLen=i+1
            d[sum]=i
        else:
            index=d[sum]
            subsetLen=i-index
        if subsetLen>maxLen:
            maxLen=subsetLen
    return maxLen


n=int(input())
l=list(int(i) for i in input().strip().split(' '))
finalLen= subsetSum(l)
print(finalLen)


# def subsetSum(l):
#     max_len = 0
#     sum = 0
#     d = {}
#     for i in range(len(l)):
#         sum += l[i]
#         if l[i]==0:
#             max_len = max(max_len,1)
#         elif sum==0:
#             max_len =max(max_len,i+1)
#         elif sum in d:
#             max_len = max(max_len,i-d[sum])
#         else:
#             d[sum] = i 
#     return max_len
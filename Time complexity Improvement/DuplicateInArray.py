def MissingNumber(a,n):
    ans1=0
    ans2=0
    for i in range(n-1):
        ans1=ans1+i
    for i in range(n):
        ans2=ans2+a[i]
    return ans2-ans1
    

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
ans=MissingNumber(arr,n)
print(ans)

# Time complexity of this approach is O(n)

def unique(a):
    if len(a)==1:
        return a
    ans=0
    for i in range(len(a)):
        ans=ans^a[i]
    return ans

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(unique(arr))
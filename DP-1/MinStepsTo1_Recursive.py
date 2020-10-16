# Given a positive integer 'n', find and return the minimum number of steps that 'n' has to take to get reduced to 1. You can perform any one of the following 3 steps:
# 1.) Subtract 1 from it. (n = n - ­1) ,
# 2.) If n is divisible by 2, divide by 2.( if n % 2 == 0, then n = n / 2 ) ,
# 3.) If n is divisible by 3, divide by 3. (if n % 3 == 0, then n = n / 3 ).  

# this is the recursive approach to this problem statment


import sys

def minSteps(n):
    if n==1:
        return 0
    
    ans1=ans2=ans3=sys.maxsize

    ans1=minSteps(n-1)

    if n%2==0:
        ans2=minSteps(n//2)
    if n%3==0:
        ans3=minSteps(n//3)
    
    ans=min(ans1,ans2,ans3)+1
    return ans


# main
sys.setrecursionlimit(1000000)
n=int(input())
dp=[-1 for i in range(n+1)]
print(minSteps(n))
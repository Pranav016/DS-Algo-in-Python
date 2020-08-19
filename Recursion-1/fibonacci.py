# print nth fibonacci number

# we can also update the recursion deph limit for large values of n:
# from sys import setrecursionlimit
# setrecursionlimit(2000)

def fibo(n):
    if n==1 or n==0:
        return n
    output=fibo(n-1)+fibo(n-2)
    return output
n=int(input())
print(fibo(n))
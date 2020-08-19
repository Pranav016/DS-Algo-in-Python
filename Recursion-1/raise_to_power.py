# print x raise to power n
def power(x,n):
    if n==0:
        return 1
    product= x*power(x,n-1)
    return product
x=int(input()) 
n=int(input())
print(power(x,n))
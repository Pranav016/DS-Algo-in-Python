from sys import stdin

def rotate(a, n, d):
    if len(a)==0:
        return 
    if d>n:
        return 
    e=a[:d]
    i=0
    j=d
    while i<n-d and j<n:
        a[i]=a[j]
        i+=1
        j+=1
    j=0
    while i<n and j<d:
        a[i]=e[j]
        i+=1
        j+=1


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    n = int(stdin.readline().rstrip())
    if n == 0:
        break
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    print(*arr)
    
    t -= 1
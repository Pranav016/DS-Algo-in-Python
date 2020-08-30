# You have been given a random integer array/list(ARR) of size N. Write a function that rotates the given array/list by D elements(towards the left).

# time complexity is O(n)

# sample input
# 1 (no of test cases)
# 7
# 1 2 3 4 5 6 7
# 2
# sample output
# 3 4 5 6 7 1 2

from sys import stdin

def rotate(a,n,rot):
    if len(a)==0:
        return
    elif rot>n:
        return

    elements=a[:rot]
    i=0
    while i<n-rot:
        a[i]=a[i+rot]
        i+=1
    
    j=0
    while i<n and j<rot:
        a[i]=elements[j]
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
# reversing a stack using another stack
import sys

def reverse(s1,s2):
    if len(s1)<=1:
        return
    while len(s1)!=1:
        x=s1.pop()
        s2.append(x)

    bottom=s1.pop()

    while s2:
        x=s2.pop()
        s1.append(x)
    
    reverse(s1,s2)
    s1.append(bottom)

# main

sys.setrecursionlimit(1000000)
s1=[]
s2=[]
n=int(input())
if n>0:
    ele=list(int(i) for i in input().split())
    for i in ele:
        s1.append(i)
    reverse(s1,s2)
    while s1:
        print(s1.pop(), end=" ")
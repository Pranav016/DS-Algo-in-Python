#A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.

def stairs(n):
    if n==0 or n==1:
        return 1
    elif n==2:
        return 2
    # elif n==3:  #this can be used to reduce the Time to prevent TLE
    #     return 4
    return stairs(n-1)+stairs(n-2)+stairs(n-3)

import sys
sys.setrecursionlimit(110000)
n=int(input())
print(stairs(n))
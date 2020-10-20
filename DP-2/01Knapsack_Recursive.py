def knapsack(weights,values,capacity,n):
    if n==0:
        return 0


    if weights[n-1]>capacity:
        return knapsack(weights,values,capacity,n-1)
    else:
        includeWt=values[n-1]+knapsack(weights,values,capacity-weights[n-1],n-1)
        notIncludeWt=knapsack(weights,values,capacity,n-1)
        return max(includeWt,notIncludeWt)

# main
n=int(input())
weights=list(int(i) for i in input().strip().split(' '))
values=list(int(i) for i in input().strip().split(' '))
maxWeight=int(input())
n=len(weights)
print(knapsack(weights, values, maxWeight,n))
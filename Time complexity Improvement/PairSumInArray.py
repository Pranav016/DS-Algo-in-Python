# sample test case-
# 9
# 1 3 6 2 5 4 3 2 4
# 7
# sample output-
# 1 6
# 3 4
# 3 4
# 2 5
# 2 5
# 3 4
# 3 4

def pairSum(a,x):

    arr.sort()

    start=0
    end=len(a)-1
    while start<end:

        if a[start]+a[end]>x:
            end-=1
        elif a[start]+a[end]<x:
            start+=1
        else:
            count1=0
            count2=0
        
            for ptr in range(start,end):
                if a[ptr]==a[start]:
                    count1+=1
                else:
                    break

            for ptr in range(end,start,-1):
                if a[ptr]==a[end]:
                    count2+=1
                else:
                    break
            
            combinations=count1*count2


            if a[start]==a[end]:
                combinations=(end-start+1)*(end-start)//2

            for i in range(combinations):
                print("{} {}".format(a[start],a[end]))
                i+=1

            start+=count1
            end-=count2


# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
pairSum(arr, sum)

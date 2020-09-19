def pairSum(a,x):
    a.sort()

    for i in range(len(a)-1):
        x=x-a[i]
        start=i+1
        end=len(a)-1

        start=0
        end=len(a)-1
        while start<end:
            if a[start]+a[end]<sum:
                start+=1
            elif a[start]+a[end]>sum:
                end-=1
            else:
                c1=0
                c2=0
                combinations=0
                for ptr in range(start,end):
                    if a[ptr]==a[start]:
                        c1+=1
                    else:
                        break

                for ptr in range(end,start,-1):
                    if a[ptr]==a[end]:
                        c2+=1
                    else:
                        break
                
                combinations=c1*c2
                if a[start]==a[end]:
                    combinations=(end-start+1)*(end-start)//2

                for i in range(combinations):
                    print("{} {}".format(a[start],a[end]))
                    i+=1

                start+=c1
                end-=c2

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
pairSum(arr, sum)
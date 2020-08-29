# 7
# 1 2 3 4 5 6 7 
# 12

def triplet(arr, sum):
    
    arr.sort() 
    
    for i in range(len(arr)-1):
        
        start = i + 1
        end = len(arr) - 1
        val = sum - arr[i]
        
        while start < end:
            
            if arr[start] + arr[end] > val:
                end -= 1
                
            elif arr[start] + arr[end] < val:
                start += 1
                
            else:
                count1 = 0
                count2 = 0
                
                for ptr in range(start, end):
                    if arr[ptr] == arr[start]:
                        count1 += 1
                    else:
                        break
                        
                for ptr in range(end, start, -1):
                    if arr[ptr] == arr[end]:
                        count2 += 1
                    else:
                        break
                        
                combinations = count1 * count2
                
                if arr[start] == arr[end]:
                    combinations = ((end-start+1)*(end-start))//2
                    
                for k in range(combinations):
                    print(arr[i], arr[start], arr[end])
                    
                start += 1
                end -= count2
                        
                




# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
triplet(arr, sum)

def permutations(string,res,ans):
    n=len(string)
    
    if n==0:
        ans.append(res)
    else:
        for i in range(n):
            newres=res+string[i]
            newstring=string[0:i]+string[i+1:]
            permutations(newstring,newres,ans)
    return ans
    

string = input()
ans=permutations(string,"",list())
for s in ans:
    print(s)
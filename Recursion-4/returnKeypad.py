def keypad(n,keys):
    if n==0:
        output=[]
        output.append("")
        return output

    newN=n//10
    lastDigit=n%10
    smalloutput=keypad(newN,keys)
    output=[]
    for string in smalloutput:
        for char in keys[lastDigit]:
            output.append(string+char)
    
    return output

# main
n = int(input())
keys=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
ans = keypad(n,keys)
for s in ans:
    print(s)
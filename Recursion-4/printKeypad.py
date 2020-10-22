def keypad(n,keys,ans):
    if n==0:
        print(ans)
        return

    newN=n//10
    lastDigit=n%10
    for char in keys[lastDigit]:
        keypad(newN,keys,char+ans)

# main
n = int(input())
keys=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
keypad(n,keys,"")
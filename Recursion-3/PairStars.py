def stars(s,i):
    if i==len(s)-1:
        print(s[i])
        return

    print(s[i],end="")    
    if s[i]==s[i+1]:
        print("*",end="")
    stars(s,i+1)

s=str(input())
stars(s,0)

#sample input - hello
#sample output- hel*lo
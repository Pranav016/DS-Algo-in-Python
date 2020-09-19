# Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".

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

# alternate- 

def stars(s):
    if len(s)<=1:
        print(s[0])
        return
    print(s[0],end='')
    if s[0]==s[1]:
        print('*',end='')
    stars(s[1:])

s=str(input())
stars(s)

#sample input - hello
#sample output- hel*lo
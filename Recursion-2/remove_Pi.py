# to understand this code, dry run with input 'ppi'

def removePi(s):
    l=len(s)
    if l==0 or l==1:
        return s
    
    if s[0]=='p' and s[1]=='i':
        smallOutput= removePi(s[2:])
        return "3.14"+smallOutput
    else:
        smallOutput= removePi(s[1:])
        return s[0]+smallOutput

s= str(input())
print(removePi(s))
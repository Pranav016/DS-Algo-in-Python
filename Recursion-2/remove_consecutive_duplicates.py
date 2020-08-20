def rcd(s):
    if len(s)<=1:
        return s
    smallOutput=rcd(s[1:])
    
    if s[0]==s[1]:
        return smallOutput
    else:
        return s[0]+smallOutput

# Main
s = input().strip()
print(rcd(s))

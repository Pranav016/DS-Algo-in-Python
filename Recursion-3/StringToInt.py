def stringToInt(n):
    if len(n)==1:
        return int(n)
    
    a=stringToInt(n[:-1])*10
    return a+int(n[-1])

n=str(input())
print(stringToInt(n))
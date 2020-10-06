def uniqueChars(string):
    d={}
    for w in string:
        d[w]=d.get(w,0)+1
    u={}
    for w in d.keys():
        if d[w]>1:
            u[w]=abs(1-d[w])
    l=len(string)-1
    newString=[]
    while l>=0:
        y=u.get(string[l],0)
        if y>0:
            u[string[l]]=u[string[l]]-1
        else:
            newString.append(string[l])
        l-=1
    newString.reverse()
    return newString

# Main
string = input()
for i in uniqueChars(string):
    print(i,end="")

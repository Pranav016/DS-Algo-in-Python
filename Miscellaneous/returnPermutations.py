# return permutations


def permutations(string):
    if len(string)==0:
        a=[[]]
        return a
    m=permutations(string[1:])
    c=[[]]
    if len(m)==1:
        v=[string[0]]
        c.append(v)
        return c
    for i in range(1,len(m)):
        a=m[i]
        for j in range(len(a)+1):
            v=a[:j]+[string[0]]+a[j:]
            c.append(v)
    return c



string = input()
ans = permutations(string)
for i in ans:
    for j in i:
        print(j,end='')
    print()
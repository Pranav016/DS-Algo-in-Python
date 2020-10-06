def maxFreq(l):
    d={}
    for w in l:
        d[w]=d.get(w,0)+1
    word=None
    max=-1000000
    for w in l:
        if d[w]>max:
            word=w
            max=d[w]
    return word 

# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))

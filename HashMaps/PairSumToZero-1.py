def freqDict(l):
    d={}
    for w in l:
        d[w]=d.get(w,0)+1
    return d

def printFreq(d,a,b):
    freqA=d[a]
    freqB=d[b]
    if a==b:
        for i in range(freqA):
            print(a,b)
    else:
        combinations=freqA*freqB
        for i in range(combinations):
            print(a,b)
            i+=1
    return freqA,freqB

def pairSum0(l):
    l.sort()
    d=freqDict(l)
    start=0
    end=len(l)-1
    while start<end:
        if l[start]+l[end]>0:
            end-=1
        elif l[start]+l[end]<0:
            start+=1
        else:
            s,e=printFreq(d,l[start],l[end])
            start+=s
            end-=e


n=int(input())
l=list(int(i) for i in input().strip().split(' '))
pairSum0(l)
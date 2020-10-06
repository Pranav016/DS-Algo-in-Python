def wordsWithFrequencyK2(words,k):
    d={}
    for w in words:
        if w in d:
            d[w]=d[w]+1
        else:
            d[w]=1
    for w in d:
        if d[w]==k:
            print(w)


def wordsWithFrequencyK1(words,k):
    d={}
    for w in words:
        d[w]=d.get(w,0)+1
    for w in d:
        if d[w]==k:
            print(w)

# main
s="hello this is a friday and it is raining so happy friday"
k=2
words=s.split()
wordsWithFrequencyK1(words,k)
# You are given an array of unique integers that contain numbers in random order. Write a program to find the longest possible sequence of consecutive numbers using the numbers from given array.
# You need to return the output array which contains consecutive elements. Order of elements in the output is not important.
# Best solution takes O(n) time.
# If two sequences are of equal length then return the sequence starting with the number whose occurrence is earlier in the array.


def longestConsecutiveSubsequence(l):
    d={}
    j=0
    for i in l:
        if d.get(i,-1)==-1:
            d[i]=[True,j]
            j+=1
    maxLen=-1000000
    start=None
    for i in l:
        smallLen=1
        tempStart=i
        j=i
        while d.get(j+1,False) and d[j+1][0]!=False:
            d[j+1][0]=False
            smallLen+=1
            j+=1
        j=i
        while d.get(j-1,False) and d[j-1][0]!=False:
            d[j-1][0]=False
            smallLen+=1
            tempStart=j-1
            j-=1
        if smallLen>maxLen:
            maxLen=smallLen
            start=tempStart
        elif smallLen==maxLen:
            if d[start][1]>d[tempStart][1]:
                start=tempStart
    return start,maxLen


n=int(input())
l=list(int(i) for i in input().strip().split(' '))
start,maxLen = longestConsecutiveSubsequence(l)
for i in range(maxLen):
    print(start+i)
# LCS- Largest Common Subsequence problem


def lcs(i,j,n,m,str1,str2):
    
    if i>=n or j>=m:
        return 0

    if str1[i]==str2[j]:
        return 1+lcs(i+1,j+1,n,m,str1,str2)
    if str1[i]!=str2[j]:
        skipStr1=lcs(i+1,j,n,m,str1,str2)
        skipStr2=lcs(i,j+1,n,m,str1,str2)
        return max(skipStr1,skipStr2)
    

# main
str1=str(input())
n=len(str1)
str2=str(input())
m=len(str2)
print(lcs(0,0,n,m,str1,str2))
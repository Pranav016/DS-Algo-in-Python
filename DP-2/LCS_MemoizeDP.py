# LCS- Largest Common Subsequence problem


def lcs(i,j,n,m,str1,str2,dp):
    
    if i>=n or j>=m:
        return 0

    if str1[i]==str2[j]:
        if dp[i+1][j+1]!=-1:
            return 1+dp[i+1][j+1]
        else:
            dp[i+1][j+1]=lcs(i+1,j+1,n,m,str1,str2,dp)
        return 1+dp[i+1][j+1]
    if str1[i]!=str2[j]:
        if dp[i+1][j]!=-1:
            skipStr1=dp[i+1][j]
        else:
            skipStr1=lcs(i+1,j,n,m,str1,str2,dp)
        if dp[i][j+1]!=-1:
            skipStr2=dp[i][j+1]
        else:
            skipStr2=lcs(i,j+1,n,m,str1,str2,dp)
        return max(skipStr1,skipStr2)
    

# main
str1=str(input())
n=len(str1)
str2=str(input())
m=len(str2)
dp=[[-1 for j in range(m+1)]for i in range(n+1)]
print(lcs(0,0,n,m,str1,str2,dp))
# Given a string, you need to remove all the duplicates. That means, the output string should contain each character only once. The respective order of characters should remain same.



def uniqueChars(string):
    ans = ''
    
    d={}
    for i in string:
        if i not in d:
            ans = ans + i
            d[i] = True
    return ans

# main
string = input()
print(uniqueChars(string))
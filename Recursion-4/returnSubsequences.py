# Logical Intuition - 1) always do the work for the smaller string and call recursion for the bigger part
# 2) we either consider the element or we don't

def subsequences(string):
    if len(string)==0:
        output=[""]
        return output

    smallOutput=string[1:] # smaller string
    smallOutput=subsequences(smallOutput) # assume that recursion will do the work so just hit the base case, get the smallest string and work on that
    output=[]
    for ele in smallOutput:
        output.append(ele) # copying elements of the returned list to the output without string[0]
    for ele in smallOutput:
        output.append(string[0]+ele) # copying elements of the returned list with the element string[0]
    return output


# main
string = input()
ans=""
ans=subsequences(string)
for ele in ans:
    print(ele)
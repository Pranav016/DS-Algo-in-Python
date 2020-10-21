
def subsequences(string):
    if len(string)==0:
        output=[]
        output.append("")
        return output

    smallOutput=string[1:]
    smallOutput=subsequences(smallOutput)
    output=[]
    for ele in smallOutput:
        output.append(ele)
    for ele in smallOutput:
        output.append(string[0]+ele)
    return output
    


# main
string = input()
ans=""
ans=subsequences(string)
for ele in ans:
    print(ele)
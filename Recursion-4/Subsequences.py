
def subsequences(string,ans):
    if len(string)==0:
        print(ans)
        return 

    subsequences(string[1:],ans+string[0])
    subsequences(string[1:],ans)


# main
string = input()
ans=""
subsequences(string,ans)

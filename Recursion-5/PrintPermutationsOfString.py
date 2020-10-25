
def permutations(string,res=""):
    n=len(string)
    
    if n==0:
        print(res)
    else:
        for i in range(n):
            newres=res+string[i]
            newstring=string[0:i]+string[i+1:]
            permutations(newstring,newres)
    

string = input()
permutations(string)
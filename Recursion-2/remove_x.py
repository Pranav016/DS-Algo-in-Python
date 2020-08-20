# Problem: Remove x from string
def removeX(string): 
    if len(string)==0:
        return string
    smallOutput=removeX(string[1:])

    if string[0]=='x':
        return ''+smallOutput
    else:
        return string[0]+smallOutput

# Main
string = input()
print(removeX(string))

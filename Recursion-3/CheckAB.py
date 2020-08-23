# Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:
# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'
# If all the rules are followed by the given string, return true otherwise return false.


def check_ab(s):
    if len(s)==0:
        return True
    if s[0]=='a':
        if len(s)==1:
            return True
        if len(s)>1 and s[1]=='a':
            return check_ab(s[1:])
        elif len(s)>2 and (s[1]=='b' and s[2]=='b'):
            return check_ab(s[1:])
    elif len(s)>=2:
        if s[0]=='b' and s[1]=='b':
            if len(s)==2:
                return True
            elif s[2]=='a':
                return check_ab(s[2:])
    else:
        return False


s=input()
if check_ab(s):
    print('true')
else:
    print('false')
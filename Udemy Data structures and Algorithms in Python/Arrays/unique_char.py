'''Unique Characters in String
Problem
Given a string,determine if it is compreised of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return false.'''


def uni_char(s):
    lookup_str={}
    for i in s:
        if i not in lookup_str:
            lookup_str[i]=1
        else:
            return False
    return True


print(uni_char("Man"))


def uni_char(s):
    u = set()
    for c in s:
        if c in u:
            return False
        else:
            u.add(c)
    return True
    pass


# another 1-line solution
def uni_char2(s):
    return len(set(s)) == len(s)
    pass
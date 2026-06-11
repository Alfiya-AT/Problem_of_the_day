def repeatedSubstringPattern(s):
    i=0
    pattern = ""
    n=len(s)
    if len(s)<=1:
        return False
    while i<n//2:
        pattern += s[i]
        plen = len(pattern)
        r=n//plen
        if (pattern*r)==s:
            print(pattern)
            return True
        i+=1
    return False

print(repeatedSubstringPattern("aba"))
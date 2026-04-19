def Remove(s = "aabbccddd"):
    res=s[0]
    left=1
    while left<len(s):
        if s[left]!=s[left-1]:
            res+=s[left]
            left+=1
        else:
            left+=1
    print(res)

Remove()
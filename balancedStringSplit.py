def balancedStringSplit(s):
    res=0
    cnt=0
    for ch in s:
        if ch == 'L':
            res+=1
        else :
            res-=1
        if res == 0:
            cnt+=1
    return cnt

s="RLRRLLRLRL"
print(balancedStringSplit(s))